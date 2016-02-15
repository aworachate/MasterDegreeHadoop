package org.apache.hadoop.mapreduce.v2.app.job.impl;
import org.apache.hadoop.mapreduce.v2.api.records.TaskId;
import java.util.*;
public class MapTaskTime {
	   private Long taskStartTime;
	   private Long taskMapFinishedTime;
	   private Long taskFinishedAllTime;
	   private TaskId taskId;
	   MapTaskTime(TaskId taskId,Long taskStartTime,Long taskMapFinishedTime,Long taskFinishedAllTime)
       {	
       		this.taskId = taskId;
       		this.taskStartTime = taskStartTime;
       		this.taskFinishedAllTime = taskFinishedAllTime;
       		this.taskMapFinishedTime = taskMapFinishedTime;
	   }
	   public Long getTaskStartTime(){
	      return this.taskStartTime;
	   }
	   public Long getTaskFinishedAllTime(){
	      return this.taskFinishedAllTime;
	   }
	   public Long getTaskMapFinishedTime(){
	      return this.taskMapFinishedTime;
	   }
	   public TaskId getTaskIdFinishMapTime(){
	      return this.taskId;
	   }
}
