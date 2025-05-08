#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = char(ord(char) - 32)
        else:
            uppercase_char = char
    print({}.format(uppercase_char, end=""))