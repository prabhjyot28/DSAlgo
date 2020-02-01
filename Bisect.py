from bisect import *

arr = [2,3,4,577,778]      #sorted arr

bisect(arr, num)   #gives right most pos at which number should be inserted O(logn)
bisect_left(arr, num)   #gives left most pos   O(logn)


insort(arr, num)   #insert the number at right most pos and maintains the list sorted O(n)
insort_left(arr, num)    #insert at left most pos  O(n)



