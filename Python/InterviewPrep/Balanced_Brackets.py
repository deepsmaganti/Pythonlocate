userinput = list(map(str,raw_input('Enter the input: ').split()))

def check_remove(n, array):
    if n in array:
        array.remove(n)
        return array
    else:
        return 0

for i in userinput:
    if i == '[':
        userinput = check_remove(']',userinput)
    elif i == '(':
        userinput = check_remove(')', userinput)
    elif i == '{':
        userinput = check_remove('}', userinput)
    else:
        continue
    if userinput == 0:
        print 'No Match'
        break


