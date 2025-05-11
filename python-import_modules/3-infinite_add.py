#!/usr/bin/python3

import sys

add = 0.0

n = len(sys.argv)

for i in range (1,n):
    add += float(sys.argv[i])

print(add)