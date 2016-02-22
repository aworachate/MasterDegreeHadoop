#Script for update speculative system in cluster
echo "sending file to namenode"
scp ~/Desktop/temp_original/hadoop-mapreduce-client-app-2.7.1.jar hduser@namenode:/usr/local/hadoop/share/hadoop/mapreduce/
scp ~/Desktop/temp_original/hadoop-common-2.7.1.jar hduser@namenode:/usr/local/hadoop/share/hadoop/common/
scp ~/Desktop/temp_original/hadoop-mapreduce-client-core-2.7.1.jar hduser@namenode:/usr/local/hadoop/share/hadoop/mapreduce/
echo "sending file to namenode complete!"
echo "sending file to datanode1"
scp ~/Desktop/temp_original/hadoop-mapreduce-client-app-2.7.1.jar hduser@datanode1:/usr/local/hadoop/share/hadoop/mapreduce/
scp ~/Desktop/temp_original/hadoop-common-2.7.1.jar hduser@datanode1:/usr/local/hadoop/share/hadoop/common/
scp ~/Desktop/temp_original/hadoop-mapreduce-client-core-2.7.1.jar hduser@datanode1:/usr/local/hadoop/share/hadoop/mapreduce/
echo "sending file to datanode1 complete!"
echo "sending file to datanode2"
scp ~/Desktop/temp_original/hadoop-mapreduce-client-app-2.7.1.jar hduser@datanode2:/usr/local/hadoop/share/hadoop/mapreduce/
scp ~/Desktop/temp_original/hadoop-common-2.7.1.jar hduser@datanode2:/usr/local/hadoop/share/hadoop/common/
scp ~/Desktop/temp_original/hadoop-mapreduce-client-core-2.7.1.jar hduser@datanode2:/usr/local/hadoop/share/hadoop/mapreduce/
echo "sending file to datanode2 complete!"
echo "sending file to datanode3"
scp ~/Desktop/temp_original/hadoop-mapreduce-client-app-2.7.1.jar hduser@datanode3:/usr/local/hadoop/share/hadoop/mapreduce/
scp ~/Desktop/temp_original/hadoop-common-2.7.1.jar hduser@datanode3:/usr/local/hadoop/share/hadoop/common/
scp ~/Desktop/temp_original/hadoop-mapreduce-client-core-2.7.1.jar hduser@datanode3:/usr/local/hadoop/share/hadoop/mapreduce/
echo "sending file to datanode3 complete!"
echo "sending file to datanode4"
scp ~/Desktop/temp_original/hadoop-mapreduce-client-app-2.7.1.jar hduser@datanode4:/usr/local/hadoop/share/hadoop/mapreduce/
scp ~/Desktop/temp_original/hadoop-common-2.7.1.jar hduser@datanode4:/usr/local/hadoop/share/hadoop/common/
scp ~/Desktop/temp_original/hadoop-mapreduce-client-core-2.7.1.jar hduser@datanode4:/usr/local/hadoop/share/hadoop/mapreduce/
echo "sending file to datanode1 complete!"
