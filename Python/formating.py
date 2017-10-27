#! /usr/bin/env python

userinput = int(raw_input("Enter an integer : "))

def formating(n):
    
    w=(len(bin(n))- 2)
    for i in range(n):
        print (str(i+1).rjust(w,' ')+' '+
               str(oct(i+1)[1:]).rjust(w,' ')+' '+str(hex(i+1)[2:].upper()).rjust(w,' ')+' '+
               str(bin(i+1)[2:]).rjust(w,' ')+' ')
    return

formating(userinput)
