#Script for update speculative system in cluster
echo "sending file to lsc000"
scp $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-app-2.7.1.jar hadoop2@lsc000.naist.jp:/usr/local/hadoop2/share/hadoop/mapreduce/
scp $HADOOP_HOME/share/hadoop/common/hadoop-common-2.7.1.jar hadoop2@lsc000.naist.jp:/usr/local/hadoop2/share/hadoop/common/
scp $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-2.7.1.jar hadoop2@lsc000.naist.jp:/usr/local/hadoop2/share/hadoop/mapreduce/
echo "sending file to namenode complete!"
