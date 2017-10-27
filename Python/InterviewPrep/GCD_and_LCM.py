
userinput = list(map(int,raw_input('Enter the numbers: ').split()))

def GCD(array):
    for i in range(min(array),1,-1):
        if array[0]%i == 0 and array[1]%i == 0:
            return i

def GCD_n(array):
    for i in range(min(array),1,-1):
        if all(j%i == 0 for j in array):
            return i

def LCM(array):
    prod = 1
    for i in array:
        prod = prod*i
    return prod/GCD(array)

gcd = GCD(userinput)
lcm = LCM(userinput)
gcd_n = GCD_n(userinput)

print "GCD of {} is {}".format(userinput,gcd)
print "LCM of {} is {}".format(userinput,lcm)