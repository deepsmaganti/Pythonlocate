# Given an unsorted integer array, find the first missing positive integer.

def sorted_array():
    num_array = []
    num = raw_input("Enter the number of elements in the array:")
    print 'Enter numbers in array: '
    for i in range(int(num)):
        n = raw_input("num" + str(i + 1) + ":")
        num_array.append(int(n))
    print 'ARRAY: ', num_array
    num_array.sort()
    print num_array
    missing_integer(num_array)


def missing_integer(arr):
    if arr[0] >= 0:
        if len(arr) > 1:
            if arr[0] + 1 == arr[1]:
                arr.pop(0)
                missing_integer(arr)
            else:
                print "First Missing Positive Element is " + str(arr[0] + 1)
        else:
            print "First Missing Positive Element is " + str(arr[0])
    else:
        arr.pop(0)
        missing_integer(arr)

sorted_array()