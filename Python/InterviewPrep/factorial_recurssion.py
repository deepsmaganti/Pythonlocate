num = int(raw_input('Enter the number to find factorial: '))


def factorial_recc(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

print (reduce(lambda x,y:x*y,range(1,(num+1))))

print (factorial(num))
print (factorial_recc(num))