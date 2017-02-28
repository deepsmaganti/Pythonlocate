#! /usr/bin/env python

'''
Given a non-negative integer num, repeatedly add all its digits until the
result has only one digit.

For example:
Given num = 89, the process is like: 8 + 9 = 17, 1 + 7 = 8. Since 2 has only
one digit, return it.
'''

userinput = int(raw_input("Enter a non-negative number : "))

# Converting integer to string to create a list of digits
def resultdigit_one(n):
    n_list = []
    
    n_str = str(n)
    for i in n_str:
        n_list.append(int(i))
    if len(n_list) > 1:
        sum_the_digits(n_list)
    else:
        print ''.join(map(str,n_list))

# Function to sum all the digits and start over again till we get the just one digit
def sum_the_digits(integer_list):
    new_n = 0
    for i in integer_list:
        new_n = int(new_n + i)
    resultdigit_one(new_n)

resultdigit_one(userinput)
