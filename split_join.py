#! /usr/bin/env python

userinput = raw_input("Enter String to split and join: ")

def split_and_join(line):
    
    a = line.split(" ")
    out = "-".join(a)
    print out
    return out

split_and_join(userinput)
