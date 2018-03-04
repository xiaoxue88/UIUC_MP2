#!/usr/bin/env python
from operator import itemgetter
import sys

current_word=None
current_count=1

# input comes from STDIN
for line in sys.stdin:
    word, count = line.strip().split('t')
    if current_word:
        if word == current_word:
            current_count += int(count)
        else:
            print "%st%d" % (current_word, current_count)
            current_count = 1

    current_word = word

if current_count > 1:
    print "%st%d" % (current_word, current_count)