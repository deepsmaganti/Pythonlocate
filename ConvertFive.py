#! /usr/bin/env python

userinput = int(raw_input("Enter an integer : "))

def convertfive(n):
    out = []
    while (n > 0):
        r = n%10
        if (r == 0):
            r = 5
            out.append(r)
        else:
            out.append(r)
        n = n/10
    out1 = out[::-1]
    print ''.join(map(str,out1))
convertfive(userinput)
