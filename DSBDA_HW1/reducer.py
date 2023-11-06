#!/usr/bin/env python3
import subprocess

current_length = None
current_longest_word = None
max_length = 0

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
                parts = line.strip().split('\t')
                if len(parts) == 2:
                    length, word = parts
                    length = int(length)

                    if current_length == length:
                        if len(word) > max_length:
                            current_longest_word = word
                            max_length = len(word)
                    else:
                        if current_length is not None:
                            # Emit the longest word for the previous length
                            print(f"{current_length}\t{current_longest_word}")
                        current_length = length
                        current_longest_word = word
                        max_length = len(word)
    except subprocess.CalledProcessError as e:
        print(f"Error running Hadoop fs -cat for {file_path}: {e}")

# Emit the longest word for the last length
if current_length is not None:
    print(f"{current_length}\t{current_longest_word}")
