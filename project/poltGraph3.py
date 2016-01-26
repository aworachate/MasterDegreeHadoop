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

infile = open("PI/DFSIO3.log", "r")
progress_t0 = [[]for x in xrange(21)]
cpu_per_time_t0 = [[]for x in xrange(21)]
write_per_time_t0 = [[]for x in xrange(21)]
finishedSize_t0 =[[]for x in xrange(21)]
write_per_done_t0 = [[]for x in xrange(21)]
task_time_t0 = [[]for x in xrange(21)]
fin_map_time_t0 = [[]for x in xrange(21)]
# progress_t1 = []
# cpu_per_time_t1 = []
# write_per_time_t1 = []
# write_per_done_t1 = []
# finishedSize_t1 =[]
# task_time_t1 = []
	#infile_temp = infile.read()
	#Taskid[num] = num
	#ydata = []
	#print outtxt
flag = -1
mapFin = -1
for line in infile.readlines():
	if line.find(":MAP:") >=0:
		temp = int(line.split("_")[4].strip())
		#print (temp)
		flag = temp
		progress_t0[flag].append(float(line.split(":")[3].strip()))
		print float(line.split(":")[3].strip())
		if float_eq(float(line.split(":")[3].strip()),0.667):
			mapFin = 1
		else:
			mapFin = -1
		#if float(line.split(":")[3].strip() < 0.667):
		#	progress_t0[flag].append(float(line.split(":")[3].strip())/0.667)
		#else:
		#	tempPro = ((float(line.split(":")[3].strip()) - 0.667)/0.333 ) + 1
		#	progress_t0[flag].append(tempPro)
	elif line.find("CPU/Time") >= 0:
		cpu_per_time_t0[flag].append(line.split(":")[1].strip())
	elif line.find("Written/Time") >= 0:
		write_per_time_t0[flag].append(line.split(":")[1].strip())
	elif line.find("FinishedSize") >= 0:
		finishedSize_t0[flag].append(line.split(":")[1].strip())
	elif line.find("Written/Done") >= 0:
		write_per_done_t0[flag].append(line.split(":")[1].strip())
	elif line.find("Task Time") >= 0:
		task_time_t0[flag].append(line.split(":")[1].strip())
		if mapFin == 1:
			fin_map_time_t0[flag].append(line.split(":")[1].strip())
	else:
		continue

infile.close()
print fin_map_time_t0
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
plt2.plot(progress_t0[0],cpu_per_time_t0[0],'bo')
plt2.plot(progress_t0[1],cpu_per_time_t0[1],'ro')
plt2.plot(progress_t0[2],cpu_per_time_t0[2],'go')
plt2.plot(progress_t0[3],cpu_per_time_t0[3],'yo')
plt2.plot(progress_t0[4],cpu_per_time_t0[4],'mo')
plt2.plot(progress_t0[5],cpu_per_time_t0[5],'ko')
plt2.plot(progress_t0[6],cpu_per_time_t0[6],'co')
plt2.plot(progress_t0[7],cpu_per_time_t0[7],'rx')
plt2.plot(progress_t0[8],cpu_per_time_t0[8],'bo')
plt2.plot(progress_t0[9],cpu_per_time_t0[9],'ro')
plt2.plot(progress_t0[10],cpu_per_time_t0[10],'go')
plt2.plot(progress_t0[11],cpu_per_time_t0[11],'yo')
plt2.plot(progress_t0[12],cpu_per_time_t0[12],'mo')
plt2.plot(progress_t0[13],cpu_per_time_t0[13],'ko')
plt2.plot(progress_t0[14],cpu_per_time_t0[14],'co')
plt2.plot(progress_t0[15],cpu_per_time_t0[15],'rx')
plt2.plot(progress_t0[16],cpu_per_time_t0[16],'bo')
plt2.plot(progress_t0[17],cpu_per_time_t0[17],'ro')
plt2.plot(progress_t0[18],cpu_per_time_t0[18],'go')
plt2.plot(progress_t0[19],cpu_per_time_t0[19],'yo')
plt2.plot(progress_t0[20],cpu_per_time_t0[20],'mo')

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
