
userinput = list(map(int,raw_input('Enter the array of numbers: ').split()))

def squares_all(array):
    out = [i*i for i in array]
    print out

squares_all(userinput)

def squares_gen(array):
    for i in array:
        yield (i*i)

gen_out = squares_gen(userinput)
print (gen_out)
print next(gen_out)
print next(gen_out)
print next(gen_out)

# generator on comprehension list
out = (i*i for i in userinput)

print next(out)
print next(out)
print next(out)
