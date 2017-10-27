import numpy

userinput = list(map(float,raw_input('Enter an array: ').split()))

def MeanElement_builtIn(array):
    return numpy.mean(array)
def MeanElement_No_builtIn(array): # O(n)
    # array.sort()
    # summ = 0
    # for i in array:
    #     summ = float(summ) + i
    summ = reduce(lambda x,y:x+y,array)
    return float(summ/len(array))

Mean_elem_builtIn = MeanElement_builtIn(userinput)
Mean_elem_wo = MeanElement_No_builtIn(userinput)
print "Mean Element from the given array using builtIn function:%.2f" % Mean_elem_builtIn
print "Mean Element from the given array without using builtIn function:%.2f" % Mean_elem_wo