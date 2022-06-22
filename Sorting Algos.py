#Why comparison based sorting algorithms are nlogn?
# Beacause we make a series of comparisons in a sorting based algorithm and minuimum height of decision tree so that we can conclude the result is O(nlogn)
# This comes from Min Leave nodes when decision tree is optimal is n! and max leave nodes in a tree of height h is 2^h .
# So 2^h >= n!   which leads us to h>=nlogn.
# https://www.youtube.com/watch?v=WffUZk1pgXE


# Selection sort
# Find the minimum element and put it in the begining.
# Time Complexity O(n^2), Space Complexity O(1), Unstable (Can occur at Swapping step)
# Can be make stable, if instead of swapping we push all the array forward.
# Best case O(n^2)
def selectionSort(A):
    for i in range(len(A)):
     
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
                 
        # Swap the found minimum element with
        # the first element       
        A[i], A[min_idx] = A[min_idx], A[i]


#-----------------------------------------------------------------------------------------------------------------#




# Insertion sort
# The way we sort cards in our hands, ie by putting every new element in its correct position.
# Time Complexity o(n^2), Space O(1), STABLE.
# Best case O(n)
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key


#-----------------------------------------------------------------------------------------------------------------#





# Bubble sort
# Repeatedly Swap adjacent elements if they are in wrong order, in every pass maximum value will ocurr at the last.
# Hence the name bubble sort, because maximum values are bubbling at the end.
# Time Complexity O(n^2), Space O(1), STABLE.
# Best case O(n)

def bubbleSort(arr):
    # Traverse through all array elements
    for i in range(n):
        swapped = False
 
        # Last i elements are already
        #  in place
        for j in range(0, n-i-1):
  
            # traverse the array from 0 to
            # n-i-1. Swap if the element
            # found is greater than the
            # next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
 
        # IF no two elements were swapped
        # by inner loop, then break
        if swapped == False:
            break


#-----------------------------------------------------------------------------------------------------------------#



# Quick Sort
# Pick an element as Pivot, partition the array around pivot value, in linear time, apply Quick Sort in both left and right side.
# Time Complexity, Best Case / Average Case - O(nlogn),  Worst Case - O(n^2)
# best case is when partition process always pick middle element as pivot.
# Worst case is, when partition process always picks the greatest or smallest element as pivot.
# Space Complexity, Considered as Constant, but actually it takes O(logn) space for call stack (logN = Height of tree stack)
# UNSTABLE.


# Why Quick Sort is preferred over Merge Sort?
# Due to space Complexity, Quick - O(logN), Merge - O(N+logN)


#partition algo for quick sort when first number is selected as pivot.

def partition(arr):
    i = 0              # i will search for element greater than pivot
    j = len(arr)-1     # j will search for element smaller than pivot.
    pivot = arr[0]

    while i<j:
        while i<len(arr):
            if arr[i]<=pivot:
                i+=1
            else:
                break

        while j>=0:
            if arr[j]>=pivot:
                j-=1
            else:
                break

        if i<j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[0], arr[j] = arr[j], arr[0]           # j is the correct position of pivot.
    print(arr)
    return j



#-----------------------------------------------------------------------------------------------------------------#

# Simple version of partition algo.
def partition(arr, l, r):
    pivot = arr[r]
    i = l
    for j in range(l, r):       # Move all elems smaller/equal to pivot in front of arr.
        if arr[j]<=pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
    arr[i], arr[r] = arr[r], arr[i]      # Now i is the correct place for pivot.
    return i



def QucikSelect(arr,l, r, k):    # Find the kth smallest element in arr in O(n)
    # if index of partitioned element is more than k, then we recur for left part.
    # If index is same as k, we have found the k-th smallest element and we return.
    # If index is less than k, then we recur for right part.
    # This reduces the expected complexity from O(n log n) to O(n), with a worst case of O(n^2).


    # if k is smaller than number of
    # elements in array
    if (k > 0 and k <= r - l + 1):

        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        index = partition(arr, l, r)

        # if position is same as k
        if (index - l == k - 1):
            return arr[index]

        # If position is more, recur
        # for left subarray
        if (index - l > k - 1):
            return QucikSelect(arr, l, index - 1, k)

        # Else recur for right subarray
        return QucikSelect(arr, index + 1, r, k - index + l - 1)

    return -1






# Merge Sort
# Divide the array into two halves, sort them and merge them.
# Time Complexity -> O(nlogn), Space Complexity - O(N+logN)
# Stable.
# Important for sorting linked lists, because no extra space required for merging two sorted linked lists.
# Used in external sorting. (Merging two very large sorted lists, (merging in chunks).)

# Iterative Merge Sort

#-----------------------------------------------------------------------------------------------------------------#


# Heap Sort
# Time class Complexity O(nlogn), Space O(1)
# UNSTABLE



#-----------------------------------------------------------------------------------------------------------------#


# Bucket Sort
# Buckets are created to store elements into them, then these buckets are sorted individually.
# Very important when numbers are uniformly distributed into range of numbers, so we put them into different buckets.

# STEPS
# 1) Create n empty buckets (Or lists).
# 2) Do following for every array element arr[i].
# .......a) Insert arr[i] into bucket[n*array[i]]
# 3) Sort individual buckets using insertion sort / Merge sort.
# 4) Concatenate all sorted buckets.
# Time Complexity = If numbers are uniformly distributed numbers can be sort in O(n) time.
# STABLE, when Underlying sorting algos are stable.




#-----------------------------------------------------------------------------------------------------------------#



# Counting Sort
# Based on counting the occurences of each val.
# Very important when range of numbers is not significantly greater than number of objects to be sorted.
# Time Complexity = O(n)
# If numbers are in range(1, n^^2) then counting sort is not useful.
# Counting Sort is used to sort integers in particular range, then here is no point for talking about Stability.





#-----------------------------------------------------------------------------------------------------------------#




# Radix Sort
#Sort the numbers from least significant digits to most significant digits and use counting sort as a subroutine to sort.

for each digit i from least significant -> most significant:
    Sort Input array using Counting Sort according to ith digit.

# Time Complexity = O(d*(n+b)), d is O(logb(k)) where k is maximum number, b is base =10, so d is maximum digits.
# For a large k, time Complexity is more than (nlogn).
# But if we take a large base b==n than we can sort the array in O(n).
# In other words, we can sort an array of integers with ranges from (1 to n^c) if numbers are represented in base n.
#hex() - to convert a decimal into 16 base.
# Note when max digits in a number d < logN , N is number of items than, Radix sort is preferred and it's very rare so Radix
# Sort is not preferred.
