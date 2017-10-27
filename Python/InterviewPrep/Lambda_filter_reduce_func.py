
mx = lambda x,y:x if x>y else y
print mx(8,5)
print mx(9,9)

# filter function:

n = [1,2,3,4,5,6]
print(list(filter(lambda i:i>2,n)))

print (reduce(lambda x,y:x*y,n))

print (reduce(lambda x,y :x if x>y else y, n))