#!/usr/bin/python3

import sys
if __name__ == "__main__":
    add = 0
    n = len(sys.argv)
    for i in range (1, n):
        add += float(sys.argv[i])
    print(add)
