#Array hashing is very important concept, can be achieved by creating a dict.
#

def ArrayHashing(arr):
        d = {}
        for i in range(len(arr)):
                if arr[i] in d:
                        d[arr[i]].append(i)
                else:
                        d[arr[i]] = [i]


#Sometimes we need to change the original array, but its expensive
#instead we can create a new arr and than assign it to orig one

def modifyArr(arr1):
        global arr
        out = []
        # fill the out array
        arr = out
        return



def binarySearch(arr, val):
	start = 0
    end = len(arr)-1
    while start<=end:
        mid = start+int((end-start)/2)
        if(arr[mid]==val):
            return mid
        elif (arr[mid]<val):
            start = mid+1
        else:
            end = mid-1

    return



def binarySearch(arr, N):
    start = 0
    end = len(arr)-1
    while(start<=end):
        mid = (start+end)//2
        if arr[mid]==N:
            return mid
        if arr[mid]<N:
            start = mid+1
        else:
            end = mid-1

    return -1


from functools import cmp_to_key
def func(a, b):
	return a-b
    

arr.sort(key = cmp_to_key(func))    #to sort usimg comaprator







from collections import Counter
# Counter is used to create a dictionary that counts the occurences of each element in the iterable object.
c = Counter('Hello')
# c is {'l':2, 'H':1, 'e':1, 'o':1}
c.elements()  ['H','e', 'l', 'l', 'o']
c.most_common(1)  [('l',2)]


from itertools import *

#chain()
# to group multiple lists together
a = []
b = []
c = []
print(list(chain(a, b, c)))  #a+b+c   but a+b+c is not efficient bcoz it creates a new list in memory.



#count, isslice
count(start, step)  #step can also be floating no. eg 0.5 , throws infinitely many nos
range(start, stop, step)  #step can only be integers
islice(count(start, step), number_of_values)  # to get some range of values from count


#compress   to compare a list with a binary filter

a = [1,2,3,4,5]
binary_filter = [1,0,0,1,0]

print(list(compress(a, binary_filter)))  [1,4]

#zip
zip(count(), data)    # [(0, data[0]),......(n, data[-1])]   zip paired up values until our shorter iterable is exhausted.
zip_longest()   #paired up upto longest iterable is present and for other it adds None.

#cycle cycle through an iterable over and over and produce infinte values
cycle([1,2,3])   # 1,2,3,1,2,3,1...................


#repeat repeats a value over and over
repeat(2)  #2,2,2,2,2........................


#permutations and combinations

#combination   order does not matters (a, b) and (b, a) are same
#permutation   order does matters (a, b) and (b, a) are different


l = ['a', 'b', 'c', 'd']
combinations(l, 2)          # gives all the different combination of 2 values from l
permutations(l, 2)			# gives all the different permutations of 2 values from l

# permutations and combinations does not repeat value, means it does not give combinations like ('a', 'a') because there
# is only ine a in our l.

# product when we allowed to repeat the number
product(l, repeat = 4)    # give us all the different ways that we could arrange the values when repeatitions is allowed 4 times.
						   # ('a', 'a', 'a', 'b')  and ('a', 'a', 'b', 'a')   are considered different.

# to get combinations with repeated values
combinations_with_replacement(l, 4)   # ('a', 'a', 'a', 'b')  and ('a', 'a', 'b', 'a')   are considered same.


#filterfalse opposite to filter, it return values for which false occured.
filterfalse(fun, l)

# accumulate   , keeps on adding cummulative sum to each value of the list

l = [1,2,3,4]
accumulate(l)  #[1,3,6,10]

# we can operator.mul as second argument to get a the running multiplication.
import operator
accumulate(l, operator.mul)   #[1,2,6,24]
