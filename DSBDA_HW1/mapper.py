#!/usr/bin/env python3
import subprocess
import re

word_pattern = re.compile(r'\b\w+\b')

# Input file paths in HDFS
input_files = [
    "/user/mouss/input/test1.txt",
    "/user/mouss/input/test2.txt",
    "/user/mouss/input/test3.txt"
]

# Iterate over the input files in HDFS and read their contents
for file_path in input_files:
    cat_command = f"hadoop fs -cat {file_path}"
    try:
        output = subprocess.check_output(cat_command, shell=True, universal_newlines=True)
        for line in output.split('\n'):
            words = word_pattern.findall(line)
            for word in words:
                # Check if the word contains only ASCII characters
                if all(ord(c) < 128 for c in word):
                    key = len(word)
                    value = word
                    print(f"{key}\t{value}")
    except subprocess.CalledProcessError as e:
        print(f"Error running Hadoop fs -cat for {file_path}: {e}")

