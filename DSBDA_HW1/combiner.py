#!/usr/bin/env python3
import subprocess

# Initialize variables for tracking the longest word and its length
current_word = None
current_length = 0

# Input file paths in HDFS
input_files = [
    "/user/mouss/input/test1.txt",
    "/user/mouss/input/test2.txt",
    "/user/mouss/input/test3.txt"
]

for file_path in input_files:
    cat_command = f"hadoop fs -cat {file_path}"
    try:
        output = subprocess.check_output(cat_command, shell=True, universal_newlines=True)
        for line in output.split('\n'):
            if line:
                length, word = line.strip().split('\t')
                length = int(length)
                
                if length >= current_length:
                    current_length = length
                    current_word = word
    except subprocess.CalledProcessError as e:
        print(f"Error running Hadoop fs -cat for {file_path}: {e}")

# Emit the longest word and its length
if current_word:
    print(f"{current_word},{current_length}")


