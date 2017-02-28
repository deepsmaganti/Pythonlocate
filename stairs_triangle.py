#! /usr/bin/env python

userinput = int(raw_input("Enter an integer : "))

def print_stairs(n):
    h = '#'
    s = ' '
    for i in range(n):
        print ((n-(i+1))*' '+(i+1)*'#')
    return 0
def print_triangle(n):
    for i in range(n):
        print ((n-(i+1))*' '+((i*2)+1)*'#'+(n-(i+1))*' ')
    return 0

print_stairs(userinput)
print_triangle(userinput)
