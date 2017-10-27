import numpy

userinput = list(map(int, raw_input('Enter an array: ').split()))


def ModeElement_builtIn(array):
    return numpy.bincount(array).argmax()


def ModeElement_No_builtIn(array):  # O(n)
    array.sort()
    array_dict = {}
    first_element = array[0]
    cnt = 1
    for i in range(len(array)-1):
        if first_element == array[i+1]:
            cnt += 1
        else:
            array_dict[first_element] = cnt
            first_element = array[i+1]
            cnt = 1
    for key, value in array_dict.items():
        if value == max(array_dict.values()):
            return key

def first_non_recurring(input):
    for i in range(len(input)):
        if input[i] not in input[(i+1):] and input[i] not in input[:i]:
            return input[i]



Mode_elem_builtIn = ModeElement_builtIn(userinput)
Mode_elem_wo = ModeElement_No_builtIn(userinput)
print "Mode Element from the given array using builtIn function:%.2f" % Mode_elem_builtIn
print "Mode Element from the given array without using builtIn function:%.2f" % Mode_elem_wo
non_recurr = first_non_recurring(userinput)
print "First non-recurring value : {}".format(non_recurr)
