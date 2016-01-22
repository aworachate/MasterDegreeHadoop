/**
* Licensed to the Apache Software Foundation (ASF) under one
* or more contributor license agreements.  See the NOTICE file
* distributed with this work for additional information
* regarding copyright ownership.  The ASF licenses this file
* to you under the Apache License, Version 2.0 (the
* "License"); you may not use this file except in compliance
* with the License.  You may obtain a copy of the License at
*
*     http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*/

package org.apache.hadoop.mapreduce.v2.app.speculate;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicLong;

import org.apache.hadoop.mapreduce.v2.api.records.JobId;
import org.apache.hadoop.mapreduce.v2.api.records.TaskAttemptId;
import org.apache.hadoop.mapreduce.v2.api.records.TaskAttemptState;
import org.apache.hadoop.mapreduce.v2.api.records.TaskId;
import org.apache.hadoop.mapreduce.v2.app.job.Job;
import org.apache.hadoop.mapreduce.v2.app.job.Task;
import org.apache.hadoop.mapreduce.v2.app.job.TaskAttempt;
import org.apache.hadoop.mapreduce.v2.app.job.event.TaskAttemptStatusUpdateEvent.TaskAttemptStatus;

//** Project
import  org.apache.hadoop.mapreduce.v2.api.records.Counters;
import  org.apache.hadoop.mapreduce.split.JobSplit.TaskSplitMetaInfo;
//import org.apache.hadoop.mapreduce.Counters;


public class LegacyTaskRuntimeEstimator_Fixed extends StartEndTimesBase {

  private final Map<TaskAttempt, AtomicLong> attemptRuntimeEstimates
      = new ConcurrentHashMap<TaskAttempt, AtomicLong>();
  private final ConcurrentHashMap<TaskAttempt, AtomicLong> attemptRuntimeEstimateVariances
      = new ConcurrentHashMap<TaskAttempt, AtomicLong>();

  @Override
  public void updateAttempt(TaskAttemptStatus status, long timestamp) {
    super.updateAttempt(status, timestamp);

    TaskAttemptId attemptID = status.id;
    TaskId taskID = attemptID.getTaskId();
    JobId jobID = taskID.getJobId();
    Job job = context.getJob(jobID);

    //**Project : 14-12-2015 **
    int numMap = job.getTotalMaps();
    int numReduce = job.getTotalReduces();
    Map<Integer ,String> allTaskInputLenght = job.getAllTaskInputLenght();
    System.out.println("Task Size >> "+allTaskInputLenght.toString());

    if (job == null) {
      return;
    }

    Task task = job.getTask(taskID);

    if (task == null) {
      return;
    }

    TaskAttempt taskAttempt = task.getAttempt(attemptID);

    if (taskAttempt == null) {
      return;
    }

    Long boxedStart = startTimes.get(attemptID);
    long start = boxedStart == null ? Long.MIN_VALUE : boxedStart;
    //**Project : 06-12-2015 **
    //System.out.println("Start Time"+start);
    // We need to do two things.
    //  1: If this is a completion, we accumulate statistics in the superclass
    //  2: If this is not a completion, we learn more about it.

    // This is not a completion, but we're cooking.
    //
    if (taskAttempt.getState() == TaskAttemptState.RUNNING) {
      // See if this task is already in the registry
      //**Project : 06-12-2015 **
      //System.out.println("RUNNING MAN!");
      //System.out.println(taskAttempt.getID()+":"+task.getType() +":"+taskAttempt.getPhase()+":"+taskAttempt.getProgress());
      //System.out.println(taskAttempt.getPhase());
      AtomicLong estimateContainer = attemptRuntimeEstimates.get(taskAttempt);
      AtomicLong estimateVarianceContainer
          = attemptRuntimeEstimateVariances.get(taskAttempt);

      if (estimateContainer == null) {
        if (attemptRuntimeEstimates.get(taskAttempt) == null) {
          attemptRuntimeEstimates.put(taskAttempt, new AtomicLong());

          estimateContainer = attemptRuntimeEstimates.get(taskAttempt);
        }
      }

      if (estimateVarianceContainer == null) {
        attemptRuntimeEstimateVariances.putIfAbsent(taskAttempt, new AtomicLong());
        estimateVarianceContainer = attemptRuntimeEstimateVariances.get(taskAttempt);
      }


      long estimate = -1;
      long varianceEstimate = -1;

      // This code assumes that we'll never consider starting a third
      //  speculative task attempt if two are already running for this task
      if (start > 0 && timestamp > start) {
        estimate = (long) ((timestamp - start) / Math.max(0.0001, status.progress));
        varianceEstimate = (long) (estimate * status.progress / 10);
      /*  System.out.println("timestamp >> "+ timestamp +
                           " start >> " + start +
                           " , status.progress >> " + status.progress+
                           " , estimate >> " +   estimate);
      */

        //**Project : 06-12-2015 **
        //System.out.println("esitmateTime:"+estimate+"varianceEstimate:"+varianceEstimate);
        if((task.getType().toString()).equals("MAP") && status.progress > 0)
          {
        //MapTaskImpl tempTask = (MapTaskImpl)task;
        //System.out.println("Info >> " +tempTask.getTaskSplitMetaInfo);
        System.out.println("Update attemptID:"+attemptID);
        Counters tempCounters = taskAttempt.getReport().getCounters();
        String FileSystemCounter = "org.apache.hadoop.mapreduce.FileSystemCounter";
        String TaskCounter = "org.apache.hadoop.mapreduce.TaskCounter";
        Long FBR = tempCounters.getCounterGroup(FileSystemCounter).getCounter("FILE_BYTES_READ").getValue();
        Long HBR = tempCounters.getCounterGroup(FileSystemCounter).getCounter("HDFS_BYTES_READ").getValue();
        Long FBW = tempCounters.getCounterGroup(FileSystemCounter).getCounter("FILE_BYTES_WRITTEN").getValue();
        Long HBW = tempCounters.getCounterGroup(FileSystemCounter).getCounter("HDFS_BYTES_WRITTEN").getValue();
        System.out.println(taskAttempt.getID()+":"+task.getType() +":"+taskAttempt.getPhase()+":"+taskAttempt.getProgress());
        System.out.println("FILE_BYTES_READ : "+FBR);
        System.out.println("HDFS_BYTES_READ : "+HBR);
        System.out.println("FILE_BYTES_WRITTEN : "+FBW);
        System.out.println("HBW_BYTES_WRITTEN : "+HBW);
        //System.out.println(tempCounters.getCounterGroup(TaskCounter));
        long process_time = timestamp - start;
        long CPU_Time = tempCounters.getCounterGroup(TaskCounter).getCounter("CPU_MILLISECONDS").getValue();
        System.out.println("CPU/Time : " + (CPU_Time/(double)process_time));
        System.out.println("Written/Time : " + ((FBW+HBW)/(double)process_time));
        long tempSize = Long.parseLong(allTaskInputLenght.get(0));
        Double finishedSize = (double)status.progress * (double)tempSize;
        System.out.println("FinishedSize : " + finishedSize);
        System.out.println("TETS");


        // Decision algorithm
        // Call method classifyType()
        // TaskIntensive 0 : I/O intensive
        // TaskIntensive 1 : CPU intensive
            int taskIntensive = 0;
            Double temp_cal = (FBR + HBR) / (double)FBW ;
            //Double temp_cal = (HBR) / (double)MOMB;
            System.out.println("Total Read / Write : " + temp_cal);
            if (temp_cal > 1.0)
                taskIntensive = 1;
            else
                taskIntensive = 0;
            switch(taskIntensive){
                case 0 : {
                System.out.println("I/O intensive");
                break;
                }
                case 1 : {
                System.out.println("CPU intensive");
                break;
                }
              }

            //long now = clock.getTime();
            long run_time = (long)(timestamp-start);
            System.out.println("Task Time : "+run_time);
            System.out.println("CPU Time : "+CPU_Time);
            System.out.println("========================================");
          }
      }
      if (estimateContainer != null) {
        estimateContainer.set(estimate);
      }
      if (estimateVarianceContainer != null) {
        estimateVarianceContainer.set(varianceEstimate);
      }
    }
  }

//Project
  private int classifyType(){
    int jobType = -1; //{ 0 = CPU Intensive , 1 = I/O Intensive}
    return jobType;
  }

  private long storedPerAttemptValue
       (Map<TaskAttempt, AtomicLong> data, TaskAttemptId attemptID) {
    TaskId taskID = attemptID.getTaskId();
    JobId jobID = taskID.getJobId();
    Job job = context.getJob(jobID);

    Task task = job.getTask(taskID);

    if (task == null) {
      return -1L;
    }

    TaskAttempt taskAttempt = task.getAttempt(attemptID);

    if (taskAttempt == null) {
      return -1L;
    }

    AtomicLong estimate = data.get(taskAttempt);

    return estimate == null ? -1L : estimate.get();

  }

  @Override
  public long estimatedRuntime(TaskAttemptId attemptID) {
    return storedPerAttemptValue(attemptRuntimeEstimates, attemptID);
  }

  @Override
  public long runtimeEstimateVariance(TaskAttemptId attemptID) {
    return storedPerAttemptValue(attemptRuntimeEstimateVariances, attemptID);
  }
}
