package org.apache.hadoop.mapreduce.v2.app.speculate;
import java.util.*;
public class GraphData {
	   private List<Double> graphPrgoress = new ArrayList<Double>();
	   private List<Double> cpuTime = new ArrayList<Double>();
	   private long firstTimeCap = 0L;
	   private long secTimeCap = 0L;
	   private long estSortExeTime = 0L;
	   GraphData()
     {
  		  for(int i=0;i<10;i++)
  		  {
  			  graphPrgoress.add(-1.0);
  			  cpuTime.add(-1.0);
  		  }
	   }
	   List<Double> getCpuTime(){
	      return cpuTime;
	   }
	   List<Double> getgraphPrgoress(){
	      return graphPrgoress;
	   }
	   void updateVaule(int index,double value){
		   if (cpuTime.get(index) > 0.0)
			   	{
				   double temp_sum = cpuTime.get(index) + value;
				   cpuTime.set(index, (double)(temp_sum/2.0));
			   	}
		   else
			     cpuTime.set(index, value);
	   }
	   double getSlope(){
		   System.out.println(cpuTime.get(2));
		   return cpuTime.get(2)/(double)0.2;
	   }
	   void addData(double pg, double cpu){
		   int temp_index = (int)((pg*10)%10);
		   updateVaule(temp_index,cpu);
	   }
	   void setFirstCap(long time)
	   {
	   		this.firstTimeCap = time;
	   }
	   long getFirstCap()
	   {
	   		return this.firstTimeCap;
	   }
	   void setSecCap(long time)
	   {
	   		this.secTimeCap = time;
	   }
	   long getSecCap()
	   {
	   		return this.secTimeCap;
	   }
	   void setEstSortExeTime(long time)
	   {
	   		this.estSortExeTime = time;
	   }
	   long getEstSortExeTime()
	   {
	   		return this.estSortExeTime;
	   }
}
