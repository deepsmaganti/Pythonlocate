userinput = list(map(int,raw_input('Enter an array: ').split()))

def maxElement_builtIn(array):
    return max(array)
def maxElement_No_builtIn(array): # O(n)
    maximum = array[0]
    for i in range(len(array)-1):
        if array[i+1] >= maximum:
            maximum = array[i+1]
    return maximum

max_elem_builtIn = str(maxElement_builtIn(userinput))
max_elem_wo = str(maxElement_No_builtIn(userinput))
print "Max Element from the given array using builtIn function:" + max_elem_builtIn
print "Max Element from the given array without using builtIn function:" + max_elem_wo
print (reduce(lambda x,y :x if x>y else y, userinput))