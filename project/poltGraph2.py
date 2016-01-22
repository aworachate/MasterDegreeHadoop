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
infile = open("PI/wordcount256mb.log", "r")
progress_t0 = []
cpu_per_time_t0 = []
write_per_time_t0 = []
finishedSize_t0 =[]
write_per_done_t0 = []
task_time_t0 = []
progress_t1 = []
cpu_per_time_t1 = []
write_per_time_t1 = []
write_per_done_t1 = []
finishedSize_t1 =[]
task_time_t1 = []
	#infile_temp = infile.read()
	#Taskid[num] = num
	#ydata = []
	#print outtxt
flag = "t0";
for line in infile.readlines():
	if line.find("attempt_1452652435059_0008_m_000000_0:MAP:") >=0:
		flag = "t0"
		progress_t0.append(line.split(":")[3].strip())
	elif line.find("attempt_1452652435059_0008_m_000001_0:MAP:") >= 0:
		flag = "t1"
		progress_t1.append(line.split(":")[3].strip())
	elif line.find("CPU/Time") >= 0:
		if flag == "t0":
			cpu_per_time_t0.append(line.split(":")[1].strip())
		elif flag == "t1":
			cpu_per_time_t1.append(line.split(":")[1].strip())
	elif line.find("Written/Time") >= 0:
		if flag == "t0":
			write_per_time_t0.append(line.split(":")[1].strip())
		elif flag == "t1":
			write_per_time_t1.append(line.split(":")[1].strip())
	elif line.find("FinishedSize") >= 0:
		if flag == "t0":
			finishedSize_t0.append(line.split(":")[1].strip())
		elif flag == "t1":
			finishedSize_t1.append(line.split(":")[1].strip())
	elif line.find("Written/Done") >= 0:
		if flag == "t0":
			write_per_done_t0.append(line.split(":")[1].strip())
		elif flag == "t1":
			write_per_done_t1.append(line.split(":")[1].strip())
	elif line.find("Task Time") >= 0:
		if flag == "t0":
			task_time_t0.append(line.split(":")[1].strip())
		elif flag == "t1":
			task_time_t1.append(line.split(":")[1].strip())
	else:
		continue

infile.close()

print (progress_t0)
print (cpu_per_time_t0)
print (write_per_time_t0)
print (finishedSize_t0)
print (write_per_done_t0)
print (task_time_t0)
print (progress_t1)
print (cpu_per_time_t1)
print (write_per_time_t1)
print (finishedSize_t1)
print (write_per_done_t1)
print (task_time_t1)


#print FILE_BYTES_WRITTEN
#print FILE_BYTES_READ
#print HDFS_BYTES_READ
#print len(FILE_BYTES_WRITTEN)
#print len(Taskid)

#plt1.plot(progress_t0,'ro')
plt2.plot(progress_t0,cpu_per_time_t0,'bo')
plt2.plot(progress_t1,cpu_per_time_t1,'ro')
#plt2.plot(progress_t0,write_per_done_t0,'go')
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
