#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args_num = len(sys.argv) - 1
    if (args_num == 0):
        print("0 arguments.")
    elif(args_num == 1):
        print("1 argument:")
    else:
        print(f"{args_num} arguments:")
    for i in range(1, len(sys.argv)):
         print(f"{i}: {sys.argv[i]}")
