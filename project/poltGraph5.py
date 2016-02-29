#!/usr/bin/python
import os
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt4
import matplotlib.pyplot as plt5
import numpy as np
#from bs4 import BeautifulSoup
#from lxml.html import parse

def float_eq(a, b, epsilon=0.00000001):
    return abs(a - b) < epsilon

infile = open("HP_Moonshot/measuer_ratio/kmean_r3_2_EWMA.log", "r")
#infile = open("pi/bay1.log", "r")
# progress_t0 = [[]for x in xrange(150)]
# cpu_per_time_t0 = [[]for x in xrange(150)]
# write_per_time_t0 = [[]for x in xrange(150)]
# finishedSize_t0 =[[]for x in xrange(150)]
# write_per_done_t0 = [[]for x in xrange(150)]
# task_time_t0 = [[]for x in xrange(150)]
# fin_map_time_t0 = [[]for x in xrange(150)]
# byte_read = [[]for x in xrange(150)]
# byte_write = [[]for x in xrange(150)]
# byte_write_per_read = [[]for x in xrange(150)]
Taskid = [] * 150
runtime = [] * 150
avg_runtime = [] * 150
ewma_avg = [] * 150
ewma_avg_from_hadoop = [] * 500
avg_runtime_from_hadoop = [] * 500
mapphasetime = [] * 150
mapratio = [] * 150
sortratio = [] * 150
avg_weight = [] * 150
ewma_avg_weight = [] * 150

#byte_write_per_read = [[]for x in xrange(150)]

# cpu_per_time_t1 = []
# write_per_time_t1 = []
# write_per_done_t1 = []
# finishedSize_t1 =[]
# task_time_t1 = []
	#infile_temp = infile.read()
	#Taskid[num] = num
	#ydata = []
	#print outtxt
#flag = -1
#mapFin = -1
ewma_avg_t0 = 0.0
ewma_avg_t1 = -1.0
alpha = 0.5

ewma_avg_weightt0 = 0.0
ewma_avg_weightt1 = -1.0
alpha_weight = 0.1

n = 0
sum = 0.0
sum_weight = 0.0
for line in infile.readlines():
	if line.find("Successful task time : task") >=0:
		n = n+1
		Taskid.append(line.split(":")[1].strip())
		runtime.append((long)(line.split(":")[3].strip()))
		sum += (int)(line.split(":")[3].strip())
		avg_runtime.append( (float)(sum) / n)
		if (n==1):
			ewma_avg_t0 = (float)(line.split(":")[3].strip())
		else:
			ewma_avg_t0 = ewma_avg_t1
		ewma_avg_t1 = (alpha * (float)(line.split(":")[3].strip())) + ((1-alpha)*ewma_avg_t0)
		ewma_avg.append(ewma_avg_t1)
		mapphasetime.append(line.split(":")[5].strip())
		mapratio.append((float)(line.split(":")[5].strip()) / (float)(line.split(":")[3].strip()))	
		sum_weight += ((float)(line.split(":")[5].strip()) / (float)(line.split(":")[3].strip()))
		avg_weight.append((float)(sum_weight) / n)
		if (n==1):
			ewma_avg_weightt0 = (float)(line.split(":")[5].strip()) / (float)(line.split(":")[3].strip())
		else:
			ewma_avg_weightt0 = ewma_avg_weightt1
		ewma_avg_weightt1 = (alpha_weight * ((float)(line.split(":")[5].strip()) / (float)(line.split(":")[3].strip()))) + ((1-alpha_weight)*ewma_avg_weightt0)
		ewma_avg_weight.append(ewma_avg_weightt1)
		sortratio.append( (1.0 - ((float)(line.split(":")[5].strip()) / (float)(line.split(":")[3].strip()))))		
		#if float(line.split(":")[3].strip() < 0.667):
		#	progress_t0[flag].append(float(line.split(":")[3].strip())/0.667)
		#else:
		#	tempPro = ((float(line.split(":")[3].strip()) - 0.667)/0.333 ) + 1
		#	progress_t0[flag].append(tempPro)
	elif line.find("Old estimate back up") >=0:
		avg_runtime_from_hadoop.append((long)(line.split(">>")[1].strip()))
	elif line.find("EMWA next back up finished time") >=0:
		ewma_avg_from_hadoop.append((float)(line.split(":")[1].strip()))
	else:
		continue

infile.close()
# fin_map_time_t0
print mapratio
print sortratio
print avg_runtime
print runtime
print max(runtime)
#print Taskid[runtime.index(984141)]
print ewma_avg
print ewma_avg_weight
print ewma_avg_from_hadoop
#print (progress_t0)
#print (cpu_per_time_t0[0])
#print (write_per_time_t0)
#print (finishedSize_t0)
#print (write_per_done_t0)
#print (task_time_t0)
# print (progress_t1)
# print (cpu_per_time_t1)
# print (write_per_time_t1)
# print (finishedSize_t1)
# print (write_per_done_t1)
# print (task_time_t1)


#print FILE_BYTES_WRITTEN
#print FILE_BYTES_READ
#print HDFS_BYTES_READ
#print len(FILE_BYTES_WRITTEN)
#print len(progress_t0[0])
#print len(cpu_per_time_t0[0])

#plt1.plot(progress_t0,'ro')
#plt2.xlim([0,1.0])
#plt2.ylim([0,1.5])

# plt2.plot(mapratio,'bo')
# plt2.plot(sortratio,'ro')
# plt2.plot(avg_weight,'go')
# plt2.plot(ewma_avg_weight,'yo')

#plt2.plot(ewma_avg,'go')
#plt2.plot(avg_runtime_from_hadoop,'bo')
plt2.plot(runtime,'ro')
plt2.plot(avg_runtime,'bo')
plt2.plot(ewma_avg_from_hadoop,'go')

#plt2.plot(progress_t0[0],'bo')
#plt2.plot(progress_t0[1],'ro')
#plt2.plot(progress_t0[2],'go')
#plt2.plot(progress_t0[3],'yo')
#plt2.plot(progress_t0[4],'mo')
# plt2.plot(progress_t0[5],'ko')
# plt2.plot(progress_t0[6],'co')
# plt2.plot(progress_t0[7],'rx')
# plt2.plot(progress_t0[8],'bo')
# plt2.plot(progress_t0[9],'ro')
# plt2.plot(progress_t0[10],'go')
# plt2.plot(progress_t0[11],'yo')
# plt2.plot(progress_t0[12],'mo')
# plt2.plot(progress_t0[13],'ko')
# plt2.plot(progress_t0[14],'co')
# plt2.plot(progress_t0[15],'rx')
# plt2.plot(progress_t0[16],'bo')
# plt2.plot(progress_t0[17],'ro')
# plt2.plot(progress_t0[18],'go')
# plt2.plot(progress_t0[19],'yo')
# plt2.plot(progress_t0[20],'mo')


#plt2.plot(progress_t1,cpu_per_time_t1,'ro')
#plt2.plot(progress_t0,write_per_done_t0,'go')
#plt2.plot(progress_t1,write_per_done_t1,'yo')
#plt3.plot(write_per_time_t0,'go')
#plt4.plot(finishedSize_t0,'ro')
#plt5.plot(write_per_done_t0,'ro')
#plt.plot(write_per_time,'go')
#plt.axis([0, 6, 0, 20])
#plt1.show()
plt2.show()
#plt3.show()
#plt4.show()
#plt5.show()
