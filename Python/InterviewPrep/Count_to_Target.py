#Given a collection of candidate numbers (C) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.
#Each number in C may only be used once in the combination

from itertools import combinations

array = list(map(int,raw_input('Enter the collections of numbers: ').split()))
target = int(raw_input('Enter the target number to combine: '))

def combination(array, target): # O(n^2)
    out = set([])
    for i in range(len(array)-1):
        for j in combinations(array,(i+1)):
            if sum(j) == target:
                new_array = list(j)
                new_array.sort()
                out.add(tuple(new_array))
    print out

def combination_optimize(array, target): # O(n)
    out = set([])
    new_array = []
    for i in range(len(array)-1):
        new_array = new_array + list(combinations(array,(i+1)))
    for j in new_array:
        j = list(j)
        if sum(j) == target:
            j.sort()
            out.add(tuple(j))
    print out

combination(array,target)
combination_optimize(array,target)
