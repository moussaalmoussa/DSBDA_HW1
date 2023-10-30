#import libraries
import sys
import re
import csv

# Initialize variables for tracking the longest word and its length (test1)
current_key = None
current_count = 0
max_length = 0
longest_word = None

# C:\Users\mouss\OneDrive\Desktop\universitycourses\MEPHI\semester3\Big Data\assignment\test1.txt
file_path1 = r'C:\Users\mouss\OneDrive\Desktop\universitycourses\MEPHI\semester3\Big Data\assignment\test1.txt'

# Define a regular expression pattern to match whole words in the input text
word_pattern = re.compile(r'\b\w+\b')

# Open the file for reading
file1 = open(file_path1, 'r')

for line in file1:
    words = word_pattern.findall(line)
    for word in words:
        # Check if the word contains only ASCII characters
        if all(ord(c) < 128 for c in word):  
            key = f"{len(word)},{word}"
            print(f"{key}\t1")

            # Combiner logic
            if key == current_key:
                current_count += 1
            else:
                if current_key:
                    print(f"{current_key}\t{current_count}")
                current_key = key
                current_count = 1

            # Reducer logic
            if len(word) > max_length:
                max_length = len(word)
                longest_word = word

# Print the result if there is a current_key
if current_key:
    print(f"{current_key}\t{current_count}")

# Print the longest word and its length
if longest_word:
    print(f"{longest_word},{max_length}")

# Save the longest word to a CSV file
if longest_word:
    with open('output1.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Longest Word', 'Length'])
        csv_writer.writerow([longest_word, max_length])
if longest_word:
    print(f"{longest_word},{max_length}")


###################################################################################
# Initialize variables for tracking the longest word and its length (test2)
current_key = None
current_count = 0
max_length = 0
longest_word = None

print()
# C:\Users\mouss\OneDrive\Desktop\universitycourses\MEPHI\semester3\Big Data\assignment\test2.txt
file_path2 = r'C:\Users\mouss\OneDrive\Desktop\universitycourses\MEPHI\semester3\Big Data\assignment\test2.txt'

# Define a regular expression pattern to match whole words in the input text
word_pattern = re.compile(r'\b\w+\b')

# Open the file for reading
file2 = open(file_path2, 'r')

for line in file2:
    words = word_pattern.findall(line)
    for word in words:
        # Check if the word contains only ASCII characters
        if all(ord(c) < 128 for c in word):  
            key = f"{len(word)},{word}"
            print(f"{key}\t1")

            # Combiner logic
            if key == current_key:
                current_count += 1
            else:
                if current_key:
                    print(f"{current_key}\t{current_count}")
                current_key = key
                current_count = 1

            # Reducer logic
            if len(word) > max_length:
                max_length = len(word)
                longest_word = word

# Print the result if there is a current_key
if current_key:
    print(f"{current_key}\t{current_count}")

# Print the longest word and its length
if longest_word:
    print(f"{longest_word},{max_length}")

# Save the longest word to a CSV file
if longest_word:
    with open('output2.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Longest Word', 'Length'])
        csv_writer.writerow([longest_word, max_length])
if longest_word:
    print(f"{longest_word},{max_length}")


###################################################################################
# Initialize variables for tracking the longest word and its length (test3)
current_key = None
current_count = 0
max_length = 0
longest_word = None

print()
# C:\Users\mouss\OneDrive\Desktop\universitycourses\MEPHI\semester3\Big Data\assignment\test3.txt
file_path3 = r'C:\Users\mouss\OneDrive\Desktop\universitycourses\MEPHI\semester3\Big Data\assignment\test3.txt'

# Define a regular expression pattern to match whole words in the input text
word_pattern = re.compile(r'\b\w+\b')

# Open the file for reading
file3 = open(file_path3, 'r')

for line in file3:
    words = word_pattern.findall(line)
    for word in words:
        # Check if the word contains only ASCII characters
        if all(ord(c) < 128 for c in word):  
            key = f"{len(word)},{word}"
            print(f"{key}\t1")

            # Combiner logic
            if key == current_key:
                current_count += 1
            else:
                if current_key:
                    print(f"{current_key}\t{current_count}")
                current_key = key
                current_count = 1

            # Reducer logic
            if len(word) > max_length:
                max_length = len(word)
                longest_word = word

# Print the result if there is a current_key
if current_key:
    print(f"{current_key}\t{current_count}")

# Print the longest word and its length
if longest_word:
    print(f"{longest_word},{max_length}")

# Save the longest word to a CSV file
if longest_word:
    with open('output3.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Longest Word', 'Length'])
        csv_writer.writerow([longest_word, max_length])
if longest_word:
    print(f"{longest_word},{max_length}")
