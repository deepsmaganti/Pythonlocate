
num = int(raw_input('Enter the end number: '))

# def fibonacci_wo_DP(n):
#
#     for i in

def fibonacci_one(n):
    if n == 0:
        return 0
    else:
        fib_array = [0,1]
        print fib_array[0]
        print fib_array[1]
        for i in range(n-2):
            new = fib_array[i] + fib_array[i+1]
            fib_array.append(new)
            print fib_array[i+2]

def fibonacci_two(n): # SC - O(1), TC - O(n)
    if n == 0:
        return 0
    else:
        x1 = 0
        x2 = 1
        print x1
        print x2
        for i in range(2,n):
            x3 = x1+x2
            x1 = x2
            x2 = x3
            print x2

def fibonacci_w_DP(n): # SC - O(1), TC - O(n)
    fib_array = [0,1]
    for i in range(n-3):
        if fib_array[i] in fib_array:
            print fib_array[i]
        else:
            fib_array[i] = fibonacci_w_DP(i-1) + fibonacci_w_DP(i-2)
            print fib_array[i]

def fibonacci_generator(n):
    fib_array = [0,1]
    for i in xrange(0,n):
        yield "{}: {}".format(i+1,fib[0])


fibonacci_two(num)
fibonacci_w_DP(num)