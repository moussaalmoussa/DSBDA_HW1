# mapper.py
#!/usr/bin/env python
import sys
import re

for line in sys.stdin:
    line = line.strip()
    words = re.findall(r'\b\w+\b', line)  # Tokenize words
    for word in words:
        if all(ord(c) < 128 for c in word):  # Check if word contains only ASCII characters
            print(f"{len(word)},{word}\t1")
