# reducer.py
#!/usr/bin/env python
import sys

max_length = 0
longest_word = None

for line in sys.stdin:
    key, count = line.strip().split('\t')
    count = int(count)
    length, word = key.split(',')
    length = int(length)

    if length > max_length:
        max_length = length
        longest_word = word

if longest_word:
    print(f"{longest_word},{max_length}")
