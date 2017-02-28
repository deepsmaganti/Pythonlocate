#! /usr/bin/env python

n = int(raw_input("Enter : "))

w = 7

print bin(n)
print str(n).rjust(w,'#')
print str(n).ljust(w,'#')
