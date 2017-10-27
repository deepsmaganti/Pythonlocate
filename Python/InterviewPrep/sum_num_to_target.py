array = list(map(int,raw_input('Enter the collections of numbers: ').split()))
target = int(raw_input('Enter the target number to combine: '))

def sum_any_two_nums(array, target):
    out = []
    #out = set([]) # if asked for unique
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            tmp = []
            if array[i] + array[j] == target:
                out.append([array[i],array[j]])
                # tmp.append(array[i]) # if asked for unique
                # tmp.append(array[j])
                # tmp.sort()
                # out.add(tuple(tmp))
    print (out)

from itertools import combinations

l = [5,2,3,9,1]

for var in combinations(l, 2):
    if var[0] + var[1] == 10:
        print var[0], var[1]


l = [7, 9, 6, 4, 2]
s = set([l[0]])
sum = 10
for num in l[1:]:
    diff = sum - num
    if diff in s:
        print num, diff
    else:
        s.add(num)

sum_any_two_nums(array,target)