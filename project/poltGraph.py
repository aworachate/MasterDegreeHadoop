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
infile = open("PI/wordcount1gb.log", "r")
progress_t0 = [[]for x in xrange(11)]
cpu_per_time_t0 = [[]for x in xrange(11)]
write_per_time_t0 = [[]for x in xrange(11)]
finishedSize_t0 =[[]for x in xrange(11)]
write_per_done_t0 = [[]for x in xrange(11)]
task_time_t0 = [[]for x in xrange(11)]
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
flag = -1;
for line in infile.readlines():
	if line.find("attempt_1452652435059_0011_m_000000_0:MAP:") >=0:
		flag = 0
		progress_t0[flag].append(line.split(":")[3].strip())
	elif line.find("attempt_1452652435059_0011_m_000001_0:MAP:") >= 0:
		flag = 1
		progress_t0[flag].append(line.split(":")[3].strip())
	elif line.find("attempt_1452652435059_0011_m_000002_0:MAP:") >= 0:
		flag = 2
		progress_t0[flag].append(line.split(":")[3].strip())
	elif line.find("attempt_1452652435059_0011_m_000003_0:MAP:") >= 0:
		flag = 3
		progress_t0[flag].append(line.split(":")[3].strip())
	elif line.find("attempt_1452652435059_0011_m_000004_0:MAP:") >= 0:
		flag = 4
		progress_t0[flag].append(line.split(":")[3].strip())
	elif line.find("attempt_1452652435059_0011_m_000005_0:MAP:") >= 0:
		flag = 5
		progress_t0[flag].append(line.split(":")[3].strip())
	elif line.find("attempt_1452652435059_0011_m_000006_0:MAP:") >= 0:
		flag = 6
		progress_t0[flag].append(line.split(":")[3].strip())
	elif line.find("attempt_1452652435059_0011_m_000007_0:MAP:") >= 0:
		flag = 7
		progress_t0[flag].append(line.split(":")[3].strip())
	elif line.find("attempt_1452652435059_0011_m_000005_1:MAP:") >= 0:
		flag = 8
		progress_t0[flag].append(line.split(":")[3].strip())
	elif line.find("attempt_1452652435059_0011_m_000004_1:MAP:") >= 0:
		flag = 9
		progress_t0[flag].append(line.split(":")[3].strip())
	elif line.find("attempt_1452652435059_0011_m_000003_1:MAP:") >= 0:
		flag = 10
		progress_t0[flag].append(line.split(":")[3].strip())
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
	else:
		continue

infile.close()

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
