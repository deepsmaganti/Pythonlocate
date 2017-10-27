#Given an array of integers:
#Rearrange the array such that all non-zero members appear on the left of the array

userinput = list(map(int,raw_input('Enter the input: ').split()))

# for i in userinput:
#     if i == 0:
#         userinput.remove(i)
#         userinput.append(0)

[[userinput.remove(i), userinput.append(0)] for i in userinput if i == 0]


#print userinput
print userinput