def quicksort(a):
    a.sort()
    print(a)


def find(array, tofind):
    if tofind in array:
        index = array.index(tofind)
        print("your index is")
        print(index)
    else:
        print("no")

def minznach(array):
    array.sort()
    print(array)
    i = 0
    while i<5:
        print(array[i])
        i = i+1

def maxznach(array):
    array.sort(reverse=True)
    print(array)
    i = 0
    while i<5:
        print(array[i])
        i = i+1

def serarifm(array):
    print(sum(array)/len(array))
    

def delete(array):
    array = list(dict.fromkeys(array))
    print(array)

def lcm(a,b):
    import math
    print((a*b) // math.gcd(a,b))

def odnakovi(array):
    import collections
    results = collections.Counter(array)
    print(results)

def cycle(array):
    e1 = array[-1]
    for i, e2 in enumerate(array):
        array[i], e1 = e1, e2
    print(array)
