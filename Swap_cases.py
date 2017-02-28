#! /usr/bin/env python

userinput = raw_input("Enter String to Swap: ")

def swap_case(s):
    string = s
    a = []
    for i in range(len(string)):
        if string[i] == string[i].lower():
            a.append(s[i].upper())
        elif string[i] == string[i].upper():
            a.append(s[i].lower())
        else:
            a.append(s[i])
    a1 = ''.join(a)
    print a1
    return a1

swap_case(userinput)

print userinput.swapcase()
