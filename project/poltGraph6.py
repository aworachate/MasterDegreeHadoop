#!/usr/bin/python
import os
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt4
import matplotlib.pyplot as plt5
import numpy as np
from array import *
#from bs4 import BeautifulSoup
#from lxml.html import parse

def float_eq(a, b, epsilon=0.00000001):
    return abs(a - b) < epsilon

infile = open("/Users/worachate-a/Desktop/temp_successtime.log", "r")
#infile = open("pi/bay1.log", "r")
progress_t0 = [[]for x in xrange(550)]
cpu_per_time_t0 = [[]for x in xrange(550)]
write_per_time_t0 = [[]for x in xrange(550)]
finishedSize_t0 =[[]for x in xrange(550)]
write_per_done_t0 = [[]for x in xrange(550)]
task_time_t0 = [[]for x in xrange(550)]
fin_map_time_t0 = [[]for x in xrange(550)]
byte_read = [[]for x in xrange(550)]
byte_write = [[]for x in xrange(550)]
byte_write_per_read = [[]for x in xrange(550)]
est_old = [[]for x in xrange(550)]
est_new = [[]for x in xrange(550)]
finished_time = array('l')
avg_mean = array('f')
# cpu_per_time_t1 = []
# write_per_time_t1 = []
# write_per_done_t1 = []
# finishedSize_t1 =[]
# task_time_t1 = []
	#infile_temp = infile.read()
	#Taskid[num] = num
	#ydata = []
	#print outtxt
flag = 0
mapFin = -1
for line in infile.readlines():
	finished_time.append((long)(line.split(":")[3].strip()))
	flag = flag + 1
	#if line.find("Esitmate Time from LATE-Algo :") >= 0:
		#print ">> ["+ str(flag) +"]" + line.split(":")[1].strip()
		#est_old[flag].append((float)(line.split(":")[1].strip())/(1000))
	# 	temp1 = (float)(line.split(":")[1].strip())/(1000)
	# if line.find("Esitmate Time from New-Algo :") >= 0:
	# 	#print ">> ["+ str(flag) +"]" + line.split(":")[1].strip()
	# 	#est_new[flag].append((float)(line.split(":")[1].strip())/(1000))
	# 	temp2 = (float)(line.split(":")[1].strip())/(1000)

	# if line.find(":MAP:") >=0:
	# 	temp = int(line.split("_")[4].strip())
	# 	#print (temp)
	# 	flag = temp 
	# 	#print line
	# 	progress_t0[flag].append(float(line.split(":")[3].strip()))
	# 	est_old[flag].append(temp1)
	# 	est_new[flag].append(temp2)
	# 	#print float(line.split(":")[3].strip())
	# 	#if float_eq(float(line.split(":")[3].strip()),0.667):
	# 	#	mapFin = 1
	# 	#else:
	# 	#	mapFin = -1
	# 	#if float(line.split(":")[3].strip() < 0.667):
	# 	#	progress_t0[flag].append(float(line.split(":")[3].strip())/0.667)
	# 	#else:
	# 	#	tempPro = ((float(line.split(":")[3].strip()) - 0.667)/0.333 ) + 1
	# 	#	progress_t0[flag].append(tempPro)
	# elif line.find("CPU/Time") >= 0:
	# 	cpu_per_time_t0[flag].append(line.split(":")[1].strip())
	# elif line.find("HDFS_BYTES_READ") >= 0:
	# 	byte_read[flag].append(line.split(":")[1].strip())
	# 	temp_read = line.split(":")[1].strip()
	# elif line.find("FILE_BYTES_WRITTEN") >= 0:
	# 	byte_write[flag].append(line.split(":")[1].strip())		
	# 	temp_write = line.split(":")[1].strip()
	# 	byte_write_per_read[flag].append(float(temp_write) / float(temp_read))
	# elif line.find("Written/Time") >= 0:
	# 	write_per_time_t0[flag].append(line.split(":")[1].strip())
	# elif line.find("FinishedSize") >= 0:
	# 	finishedSize_t0[flag].append(line.split(":")[1].strip())
	# elif line.find("Written/Done") >= 0:
	# 	write_per_done_t0[flag].append(line.split(":")[1].strip())
	# elif line.find("Successful task time :") >= 0:
	# 	finished_time[flag].append(line.split(":")[3].strip())
	# elif line.find("Task Time") >= 0:
	# 	#print ">> ["+ str(flag) +"]" + line.split(":")[1].strip()
	# 	task_time_t0[flag].append(line.split(":")[1].strip())
	# 	#if mapFin == 1:
	# 	#	fin_map_time_t0[flag].append(line.split(":")[1].strip())
	# else:
	# 	continue

infile.close()
#print len(progress_t0[0])
#print len(task_time_t0[0])
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
finished_time = sorted(finished_time)
print (finished_time)

#print FILE_BYTES_WRITTEN
#print FILE_BYTES_READ
#print HDFS_BYTES_READ
#print len(FILE_BYTES_WRITTEN)
#print len(progress_t0[0])
#print len(cpu_per_time_t0[0])

#plt1.plot(progress_t0,'ro')
#plt2.xlim([0,1.0])

#plt2.ylim([0,1000])
#plt2.ylim([0,1.4])
#plt2.ylim([0,500])
#plt2.xlim(0,150000)

# plt2.plot(task_time_t0[0],progress_t0[0],'bo')
# plt2.plot(task_time_t0[1],progress_t0[1],'go')
# plt2.plot(task_time_t0[2],progress_t0[2],'yo')
# plt2.plot(task_time_t0[4],progress_t0[4],'ro')
# plt2.plot(task_time_t0[5],progress_t0[5],'bx')
# plt2.plot(task_time_t0[6],progress_t0[6],'gx')
# plt2.plot(task_time_t0[7],progress_t0[7],'yx')
# plt2.plot(task_time_t0[80],progress_t0[80],'rx')

#plt2.plot(task_time_t0[63],progress_t0[63],'rx')
for i in xrange(0,121):
	if i == 0:
		avg_mean.append((float)(finished_time[0]))
	else:
		avg_mean.append(np.mean(finished_time[0:i+1]))
print avg_mean
plt2.plot(finished_time,'rx')
plt2.plot(avg_mean,'gx')
	
# print len(task_time_t0[35])
# print len(est_old[35])
# print len(est_new[35])
# print (task_time_t0[35])
# print (est_old[35])
# print (est_new[35])

# plt2.plot(task_time_t0[48],est_old[48],'r')
# plt2.plot(task_time_t0[48],est_new[48],'g')
# plt2.axhline(y=103,xmin=0,xmax=3,c="blue",linewidth=2.5,zorder=0)

#plt2.plot(progress_t0[1],task_time_t0[1],'ro')
#plt2.plot(progress_t0[2],task_time_t0[2],'go')
#plt2.plot(progress_t0[3],'yo')
#plt2.plot(progress_t0[4],task_time_t0[4],'mo')
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
