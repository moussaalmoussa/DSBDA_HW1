#!/bin/bash

# Local path to the input files directory
local_input_directory="/home/moussa/Desktop/Big_data_task/DSBDA_HW1/"

# HDFS destination URI to copy the files
hdfs_uri="hdfs://localhost:9000"

# HDFS destination directory
hdfs_destination="/user/mouss/input/"

# Check if the HDFS destination directory exists, and create it if not
hadoop fs -test -d "${hdfs_uri}/${hdfs_destination}"
if [ $? -ne 0 ]; then
    hadoop fs -mkdir -p "${hdfs_uri}/${hdfs_destination}"
    if [ $? -eq 0 ]; then
        echo "HDFS destination directory created: ${hdfs_destination}"
    else
        echo "Error creating HDFS destination directory: ${hdfs_destination}"
        exit 1
    fi
fi

# Iterate over the test files and copy each one to HDFS
for file in test1.txt test2.txt test3.txt; do
    hadoop fs -copyFromLocal "${local_input_directory}${file}" "${hdfs_uri}${hdfs_destination}${file}"
    if [ $? -eq 0 ]; then
        echo "File $file copied to HDFS successfully."
    else
        echo "Error copying file $file to HDFS."
    fi
done

