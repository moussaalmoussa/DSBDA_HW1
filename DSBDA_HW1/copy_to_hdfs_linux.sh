#!/bin/bash

# Local path to the input file
local_input_file="/C:\Users\mouss\OneDrive\Desktop\universitycourses\MEPHI\semester3\Big Data\assignment/test.txt"

# HDFS destination path to copy the file
hdfs_destination="/user/mouss/input/"

# Use the Hadoop HDFS command to copy the file to HDFS
hadoop fs -copyFromLocal $local_input_file $hdfs_destination
