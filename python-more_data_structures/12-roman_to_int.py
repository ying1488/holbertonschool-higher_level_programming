#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string == "":
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':
             500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40,
             'XC': 90, 'CD': 400, 'CM': 900}
    sum = 0
    prevVal = 0

    for i in reversed(roman_string):
        val = roman.get(i, 0)
        if val < prevVal:
            sum -= val
        else:
            sum += val
        prevVal = val
    return sum
