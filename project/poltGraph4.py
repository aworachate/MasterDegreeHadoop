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

infile = open("/Users/worachate-a/Desktop/temp/temp25.log", "r")
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
est_slm = [[]for x in xrange(550)]
real_progress = [[]for x in xrange(550)]
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
temp1 = -1
temp2 = -1
temp3 = -1
for line in infile.readlines():
	if line.find("Esitmate Time from LATE-Algo :") >= 0:
		#print ">> ["+ str(flag) +"]" + line.split(":")[1].strip()
		#est_old[flag].append((float)(line.split(":")[1].strip())/(1000))
		temp1 = (float)(line.split(":")[1].strip())/(1000)
	if line.find("Esitmate Time from SLM-Algo :") >= 0:
		#print ">> ["+ str(flag) +"]" + line.split(":")[1].strip()
		#est_old[flag].append((float)(line.split(":")[1].strip())/(1000))
		temp3 = (float)(line.split(":")[1].strip())/(1000)
	if line.find("Esitmate Time from New-Algo :") >= 0:
		#print ">> ["+ str(flag) +"]" + line.split(":")[1].strip()
		#est_new[flag].append((float)(line.split(":")[1].strip())/(1000))
		temp2 = (float)(line.split(":")[1].strip())/(1000)
	if line.find("Real progress") >= 0:
		#print ">> ["+ str(flag) +"]" + line.split(":")[1].strip()
		#est_new[flag].append((float)(line.split(":")[1].strip())/(1000))
		temp_real_progress = (float)(line.split(":")[2].strip())
		#print temp_real_progress

	if line.find(":MAP:") >=0:
		temp = int(line.split("_")[4].strip())
		#print 
		if int((line.split("_")[5].strip())[0])==1:
			temp = 549
		#print (temp)
		flag = temp 
		#print line
		progress_t0[flag].append(float(line.split(":")[3].strip()))
		if temp2 > temp1 or temp2 > temp3:
			print flag
		est_old[flag].append(temp1)
		est_new[flag].append(temp2)
		est_slm[flag].append(temp3)
		real_progress[flag].append(temp_real_progress)
		#print float(line.split(":")[3].strip())
		#if float_eq(float(line.split(":")[3].strip()),0.667):
		#	mapFin = 1
		#else:
		#	mapFin = -1
		#if float(line.split(":")[3].strip() < 0.667):
		#	progress_t0[flag].append(float(line.split(":")[3].strip())/0.667)
		#else:
		#	tempPro = ((float(line.split(":")[3].strip()) - 0.667)/0.333 ) + 1
		#	progress_t0[flag].append(tempPro)
	elif line.find("CPU/Time") >= 0:
		cpu_per_time_t0[flag].append(line.split(":")[1].strip())
	elif line.find("HDFS_BYTES_READ") >= 0:
		byte_read[flag].append(line.split(":")[1].strip())
		temp_read = line.split(":")[1].strip()
	elif line.find("FILE_BYTES_WRITTEN") >= 0:
		byte_write[flag].append(line.split(":")[1].strip())		
		temp_write = line.split(":")[1].strip()
		byte_write_per_read[flag].append(float(temp_write) / float(temp_read))
	elif line.find("Written/Time") >= 0:
		write_per_time_t0[flag].append(line.split(":")[1].strip())
	elif line.find("FinishedSize") >= 0:
		finishedSize_t0[flag].append(line.split(":")[1].strip())
	elif line.find("Written/Done") >= 0:
		write_per_done_t0[flag].append(line.split(":")[1].strip())
	elif line.find("Task Time") >= 0:
		#print ">> ["+ str(flag) +"]" + line.split(":")[1].strip()
		task_time_t0[flag].append(line.split(":")[1].strip())
		#if mapFin == 1:
		#	fin_map_time_t0[flag].append(line.split(":")[1].strip())
	else:
		continue

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
# print (task_time_t1)


#print FILE_BYTES_WRITTEN
#print FILE_BYTES_READ
#print HDFS_BYTES_READ
#print len(FILE_BYTES_WRITTEN)
#print len(task_time_t0[0])
#print len(real_progress[0])

#plt1.plot(progress_t0,'ro')
#plt2.xlim([0,1.0])

plt2.ylim([0,2000])
#plt2.ylim([0,1.4])
#plt2.xlim(0,150000)
# for i in xrange(0,121,5):
# 	plt2.plot(task_time_t0[0+i],progress_t0[0+i],'bo')
# 	plt2.plot(task_time_t0[1+i],progress_t0[1+i],'go')
# 	plt2.plot(task_time_t0[2+i],progress_t0[2+i],'yo')
# 	plt2.plot(task_time_t0[3+i],progress_t0[3+i],'ro')
# 	plt2.plot(task_time_t0[4+i],progress_t0[4+i],'bx')
# plt2.plot(task_time_t0[6],progress_t0[6],'gx')
# plt2.plot(task_time_t0[7],progress_t0[7],'yx')
# plt2.plot(task_time_t0[80],progress_t0[80],'rx')

#plt2.plot(task_time_t0[8],progress_t0[8],'rx')
#plt2.plot(task_time_t0[27],real_progress[27],'rx')

# print len(task_time_t0[35])
#print (est_old)
#print (est_new)
# print (task_time_t0[35])

# temp_fin_time = []
# for i in xrange(0,120):
# 	length = len(task_time_t0[i])
# 	temp_fin_time.append(est_new[i][length-1])
# 	#print sort_index

# sort_index = np.argsort(temp_fin_time)
# print sort_index

#WordCount
#1459744385479_0023
#97,70,13

#KMean clustering
#1459785769194_0019
#57,45,67

#Inverted Index
#1459744385479_0034
#110,10,5

#PageRank
#1459785769194_0063
#140,70,3

for i in xrange(70,71):
#for i in sort_index[115:120]:
	#print i
	#print (est_old[i])
	#if max(est_new[i]) > 900:
	#	print (i)
	plt2.plot(task_time_t0[i],est_new[i],'go')
	plt2.plot(task_time_t0[i],est_slm[i],'bx')
	plt2.plot(task_time_t0[i],est_old[i],'r*')
	length = len(task_time_t0[i])
	real = est_new[i][length-1]
	#print real
	plt2.axhline(y=real,xmin=0,xmax=3,c="blue",linewidth=1.5,zorder=0)

# plt2.plot(task_time_t0[67],est_old[67],'r')
# plt2.plot(task_time_t0[67],est_new[67],'g')
# plt2.axhline(y=288,xmin=0,xmax=3,c="blue",linewidth=0.5,zorder=0)

# plt2.plot(task_time_t0[1],est_old[1],'r')
# plt2.plot(task_time_t0[1],est_new[1],'g')
# plt2.plot(task_time_t0[2],est_old[2],'r')
# plt2.plot(task_time_t0[2],est_new[2],'g')




#plt2.plot(progress_t0[1],task_time_t0[1],'ro')
#plt2.plot(progress_t0[2],task_time_t0[2],'go')
#plt2.plot(progress_t0[3],'yo')
#plt2.plot(progress_t0[4],task_time_t0[4],'mo')
# plt2.plot(progress_t0[5],'ko')
# plt2.plot(progress_t0[6],'co')
# plt2.plot(progress_t0[7],'rx')
# plt2.plot(progress_t0[8],'bo')1459785769194_0063
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
