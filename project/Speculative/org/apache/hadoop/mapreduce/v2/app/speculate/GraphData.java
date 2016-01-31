package org.apache.hadoop.mapreduce.v2.app.speculate;
import java.util.*;
public class GraphData {
	   private List<Long> graphPrgoress = new ArrayList<Long>();
	   private List<Long> cpuTime = new ArrayList<Long>();
	   GraphData()
     {
  		  for(int i=0;i<10;i++)
  		  {
  			  graphPrgoress.add((long)-1.0);
  			  cpuTime.add((long)-1.0);
  		  }
	   }
	   List<Long> getCpuTime(){
	      return cpuTime;
	   }
	   List<Long> getgraphPrgoress(){
	      return graphPrgoress;
	   }
	   void updateVaule(int index,Long value){
		   if (cpuTime.get(index) > 0.0)
			   	{
				   Long temp_sum = cpuTime.get(index) + value;
				   cpuTime.set(index, (long)(temp_sum/2.0));
			   	}
		   else
			     cpuTime.set(index, value);
	   }
	   Long getSlope(){
		   System.out.println(cpuTime.get(2));
		   return cpuTime.get(2)/(long)0.2;
	   }
	   void addData(Long pg, Long cpu){
		   int temp_index = (int)((pg*10)%10);
		   updateVaule(temp_index,cpu);
	   }
}
