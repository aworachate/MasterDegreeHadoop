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
import org.apache.hadoop.mapreduce.v2.app.job.impl.MapTaskTime;
//import org.apache.hadoop.mapreduce.v2.app.job.GraphData;
//import org.apache.hadoop.mapreduce.Counters;


public class LegacyTaskRuntimeEstimator_Fixed extends StartEndTimesBase {

  private final Map<TaskAttempt, AtomicLong> attemptRuntimeEstimates
      = new ConcurrentHashMap<TaskAttempt, AtomicLong>();
  private final ConcurrentHashMap<TaskAttempt, AtomicLong> attemptRuntimeEstimateVariances
      = new ConcurrentHashMap<TaskAttempt, AtomicLong>();

  private Map<TaskAttempt, GraphData> allAttemtGraphData = new ConcurrentHashMap<TaskAttempt,GraphData>();
  private GraphData singleGraphData = new GraphData();

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
    //System.out.println("Task Size >> "+allTaskInputLenght.toString());
    //Map<Integer ,String> allTaskInputLocation = job.getAllTaskInputLocation();
    //System.out.println("Task Location 1 >> "+allTaskInputLocation.toString());
    //Map<Integer ,String> allTaskInputSplitLocation = job.getAllTaskInputSplitLocation();
    //System.out.println("Task Location 2 >> "+allTaskInputSplitLocation.toString());    

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

      //GraphData
      GraphData attemptGraphData = allAttemtGraphData.get(taskAttempt);
      if (attemptGraphData == null)
        {
          if (allAttemtGraphData.get(taskAttempt) == null)
            {
                allAttemtGraphData.put(taskAttempt,new GraphData());
                attemptGraphData = allAttemtGraphData.get(taskAttempt);
            }
        }

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
        //System.out.println("Number of complete Map Task! " + job.getCompletedMaps());
        
        boolean isDynamicEnable = false;
        float dynamic_weight = 0.0f;
        if (job.getCompletedMaps() > 0)
          {
              //long temp_sum_totaltime = 0L;
              //long temp_sum_mapFinishedtime = 0L;
              float temp_sum_map_ratio = 0.0f;
              float temp_sum_sort_ratio = 0.0f;
              float avg_map_runtime = 0.0f;
              float avg_sort_runtime = 0.0f;
              //float avg_runtime2 = 0.0f;
              //float avg_mapfinishedtime2 = 0.0f;
              Map<Integer,MapTaskTime> temp_AllFinishedMapTime = job.getAllFinishedMapTime();
              for (Map.Entry<Integer, MapTaskTime> e : temp_AllFinishedMapTime.entrySet())
                  {
                    //System.out.println(e.getValue().getTaskIdFinishMapTime() + " : " + e.getValue().getTaskFinishedAllTime() + " Running time : " + ((e.getValue().getTaskFinishedAllTime()) - (e.getValue().getTaskStartTime())) + " Map Finished Time " + ((e.getValue().getTaskMapFinishedTime()) - (e.getValue().getTaskStartTime())));
                    //System.out.println((e.getValue().getTaskMapFinishedTime()) + " start time " +  (e.getValue().getTaskStartTime()));
                    //temp_sum_totaltime += ((e.getValue().getTaskFinishedAllTime()) - (e.getValue().getTaskStartTime()));
                    //temp_sum_mapFinishedtime += ((e.getValue().getTaskMapFinishedTime()) - (e.getValue().getTaskStartTime()));
                    temp_sum_map_ratio += (((e.getValue().getTaskMapFinishedTime()) - (e.getValue().getTaskStartTime()))) / (float)(((e.getValue().getTaskFinishedAllTime()) - (e.getValue().getTaskStartTime())));
                    temp_sum_sort_ratio += ((((e.getValue().getTaskFinishedAllTime()) - (e.getValue().getTaskStartTime()))) - ((((e.getValue().getTaskMapFinishedTime()) - (e.getValue().getTaskStartTime())))))/ (float)(((e.getValue().getTaskFinishedAllTime()) - (e.getValue().getTaskStartTime())));
                  }

              //avg_runtime = temp_sum_totaltime / (float)job.getCompletedMaps();
              //avg_mapfinishedtime = temp_sum_mapFinishedtime / (float)job.getCompletedMaps();
              avg_map_runtime = temp_sum_map_ratio / (float)job.getCompletedMaps();
              avg_sort_runtime = temp_sum_sort_ratio / (float)job.getCompletedMaps();
              //dynamic_weight = avg_mapfinishedtime / avg_runtime;
              dynamic_weight = avg_map_runtime;
              //System.out.println(dynamic_weight + " VS. " + avg_runtime2 + " , " + ((avg_runtime - avg_mapfinishedtime)/avg_runtime) + " VS. " + avg_mapfinishedtime2);
              //System.out.println("Average runtime = " + avg_runtime + " Average MapPhasetime = " + avg_mapfinishedtime + " Dynamic Weight = " + dynamic_weight + ":" + ((avg_runtime - avg_mapfinishedtime)/avg_runtime));   
              isDynamicEnable = true;
          }
        // Progject dynamic weight
        float reverse_progress = 0.0f;
        float new_progress = 0.0f;
        //float new_weight = 0.995f;
        //float new_weight = 0.97f;
        //float new_weight = 0.99f;
        float new_weight = 0.667f;
        //If Complete Map Task != 0 , use Dynamic Weight, else use Default 66.7:33.3
        if (isDynamicEnable)
            {
              new_weight = dynamic_weight;
            }
        if (status.progress < 0.667f)
            {
              reverse_progress = status.progress * 1.5f;
              //System.out.println("T1 Old Progress : " + status.progress + " , Real progress : " +  reverse_progress);
              new_progress = new_weight * reverse_progress;
            } 
        else if (status.progress == 0.667f)
            {
              reverse_progress = 1.0f;
              //System.out.println("T2 Old Progress : " + status.progress + " , Real progress : " +  reverse_progress);
              new_progress = new_weight * reverse_progress;
            }
        else if (status.progress > 0.667f)
             {
              reverse_progress = (status.progress - 0.667f)*3.0f ;
              //System.out.println("T3 Old Progress : " + status.progress + " , Real progress : " +  reverse_progress);
              new_progress = new_weight + (1.0f - new_weight)*(reverse_progress);
            }         

        estimate = (long) ((timestamp - start) / Math.max(0.0001, status.progress));
        varianceEstimate = (long) (estimate * status.progress / 10);

        // Progject dynamic weight
        long estimate_new = (long) ((timestamp - start) / Math.max(0.0001, new_progress));
        long varianceEstimate_new = (long) (estimate * new_progress / 10);
        System.out.println("Esitmate Time from LATE-Algo : " + estimate);
        System.out.println("Esitmate Time from New-Algo : " + estimate_new);  
        estimate = estimate_new;
        varianceEstimate = varianceEstimate_new;  


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
            //System.out.println("FILE_BYTES_READ : "+FBR);
            //System.out.println("HDFS_BYTES_READ : "+HBR);
            //System.out.println("FILE_BYTES_WRITTEN : "+FBW);
            //System.out.println("HBW_BYTES_WRITTEN : "+HBW);
            //System.out.println(tempCounters.getCounterGroup(TaskCounter));
            long process_time = timestamp - start;
            long CPU_Time = tempCounters.getCounterGroup(TaskCounter).getCounter("CPU_MILLISECONDS").getValue();
            //System.out.println("CPU/Time : " + (CPU_Time/(double)process_time));
            //System.out.println("Written/Time : " + ((FBW+HBW)/(double)process_time));
            //long tempSize = Long.parseLong(allTaskInputLenght.get(0));
            //Double finishedSize = (double)status.progress * (double)tempSize;
            //System.out.println("FinishedSize : " + finishedSize);
            //System.out.println("Add graph Data" + status.progress + " <> " +(CPU_Time/(double)process_time));
            attemptGraphData.addData(status.progress,(CPU_Time/(double)process_time));
            //singleGraphData.addData(status.progress,(CPU_Time/(double)process_time));
            // Decision algorithm
            // Call method classifyType()
            // TaskIntensive 0 : I/O intensive
            // TaskIntensive 1 : CPU intensive
            if (Double.compare(attemptGraphData.getSlope(), 3.0) >= 0)
              {
                System.out.println("CPU Intensive");
                // Calculate estimated time  for CPU Intensive Task
                //long estimate_total_time = estimateCurr() + estimateNext();
              }
            else
              {
                System.out.println("I/O Intensive");
                // Calculate estimated time  for CPU Intensive Task
              }

            //long now = clock.getTime();
            long run_time = (long)(timestamp-start);
            System.out.println("Task Time : "+run_time);
            //System.out.println("CPU Time : "+CPU_Time);
            //System.out.println("pair : (" +new_progress+","+ estimate+")");
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

  private long storedPerAttemptValue
       (Map<TaskAttempt, AtomicLong> data, TaskAttemptId attemptID) {
    TaskId taskID = attemptID.getTaskId();
    JobId jobID = taskID.getJobId();
    Job job = context.getJob(jobID);

    Task task = job.getTask(taskID);

    if (task == null) {
      //Project
      //System.out.println("No Task in estimate array");
      return -1L;
    }

    TaskAttempt taskAttempt = task.getAttempt(attemptID);

    if (taskAttempt == null) {
      //Projec
      //System.out.println("No Task Attem in estimate array");
      return -1L;
    }

    AtomicLong estimate = data.get(taskAttempt);
    //Project
    //if (estimate == null)
      //System.out.println("No Task estimate time in estimate array due to no progress");
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
