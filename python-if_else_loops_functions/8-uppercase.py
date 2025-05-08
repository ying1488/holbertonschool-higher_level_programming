#!/usr/bin/python3
def uppercase(str):
    uppercase_char = ""
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char += "{}".format(chr(ord(char) - 32))
        else:
            uppercase_char += "{}".format(char)
    print("{}".format(uppercase_char))
