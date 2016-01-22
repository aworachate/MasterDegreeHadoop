import os
import subprocess
path1 = "org/apache/hadoop/mapred/"
flie_list = ""
for file in os.listdir(path1):
    if file.endswith(".class"):
        temp = file.replace("$", "\\$")
        flie_list = flie_list+(path1+temp+" ")
print(flie_list)
out = "$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-2.7.1.jar"
str_command="jar -uf "+out+" "+flie_list
#str_command = "javac -cp `hadoop classpath` -d "+out+" "+src

command = str_command  # the shell command

process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

#Launch the shell command:
output = process.communicate()

print output[0]
