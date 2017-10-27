# input "thiisiissaa", returns i i s a
# input "thiiissisa" returns i
# input "abcde" returns a b c d e.

userinput = raw_input("Enter the input:")
output = []
for i in range(len(userinput)-1):
    if userinput[i] == userinput[i+1]:
        output.append(userinput[i])
print (' '.join(output))
