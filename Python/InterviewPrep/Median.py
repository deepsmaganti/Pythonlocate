import numpy

userinput = list(map(float,raw_input('Enter an array: ').split()))

def medianElement_builtIn(array):
    return numpy.median(array)
def medianElement_No_builtIn(array): # O(1)
    array.sort()
    if len(array)%2 == 0:
        median = float((array[len(array)/2] + array[(len(array)/2)-1]))/2.0
    else:
        median = float(array[len(array)/2])
    return median

median_elem_builtIn = str(medianElement_builtIn(userinput))
median_elem_wo = str(medianElement_No_builtIn(userinput))
print "Median Element from the given array using builtIn function:" + median_elem_builtIn
print "Median Element from the given array without using builtIn function:" + median_elem_wo