#!/usr/bin/env python

import sys
import string



stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

Stopwords=[]
with open(stopWordsPath) as f:
    for word in f:
        Stopwords.extend(word.strip().split())


Delimiter=[]
with open(delimitersPath) as f:
    for r in f:
        for x in r.strip():
            Delimiters.append(x)
Delimiters=tuple(Delimiters)

def tsplit(string, Delimiters):
###Behaves str.split but supports multiple delimiters.###
    stack = [""]
    for i in xrange(len(string)):
        if string[i] in Delimiters:
            stack.append("")
        else:
            stack[-1] += string[i]
    return stack

for line in sys.stdin:
    for line in data:
            words_ini=tsplit(line.lower().strip(), Delimiters)
            words=filter(str.strip, words_ini)
            for word in words:
                if word not in Stopwords:
                    print "%st%d" % (word, 1)

