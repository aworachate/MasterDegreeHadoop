import os
import subprocess
path = ["hadoop-common-2.7.1/","hadoop-mapreduce-client-app-2.7.1/","hadoop-mapreduce-client-common-2.7.1/","hadoop-mapreduce-client-core-2.7.1/"]
for i in xrange(0,len(path)):
    src = ""
    for file in os.listdir("src/"+path[i]):
        if file.endswith(".java"):
            src = src+("src/"+path[i]+file+" ")
    print(src)
    #compile
    out = "output/"+path[i]
    str_command = "javac -cp `hadoop classpath` -d "+out+" "+src
    command = str_command  # the shell command
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
    #Launch the shell command:
    output = process.communicate()
    print output[0]
