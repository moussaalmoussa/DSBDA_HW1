@echo off

rem Local path to your input file
set local_input_file=C:\Users\mouss\OneDrive\Desktop\universitycourses\MEPHI\semester3\Big Data\assignment\test.txt

rem Replace 'your_hadoop_username' with your actual Hadoop username
set hadoop_username=mouss

rem HDFS destination path where you want to copy the file
set hdfs_destination=/user/%hadoop_username%/input/

rem Hadoop fs command to copy the file to HDFS
hadoop fs -copyFromLocal "%local_input_file%" %hdfs_destination%

rem Check if the copy was successful
if %errorlevel% equ 0 (
    echo File copied to HDFS successfully.
) else (
    echo Error copying file to HDFS.
)
