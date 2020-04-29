
# take two pointers, one to represent head and tail of window,
# increase the tail pointer untill found a valid window, when a window becomes valid incraese the head pointer till its valid.


# Count Subarray Problems
# count += (right - left +1)
# For every index find it's left most index ans increase count as (right - left +1 ) as there are that many subarrays between this range.


# Count number of pairs in sorted list
# count += (right - left)
# nums are in sorted order, we need to find number of pairs with diff <=k.
# for every right index calculate the left most index such that nums[right]-nums[left]<=k ans incease count as (right - left).

# Eg.  [1,2,3,4,5,8,12,16]  k=6
# l=0, r=1, count =1
# l=0, r=2, count = 2



#Using Double Sliding Window.
# Problems - Subarray with k diiferent Integers, Subarrays with k odd numbers.
# Approach - exactly(k) = atmost(k) - atmost(k-1), Use double sliding window, one for atomst k another for atmost k-1.
# for evry right index we have two lefts x1 and x2 which represents atmost(k) and atmost(k-1),
# count += (x2 - x1)  subarrays, at each iterations.




# Monotonic stack

# when we want to get next greater element we keep our stack in increasing order. (or other words first element of stack is minimum.)
# when we want next smaller element, we want to keep our stack in decreasing order. (first element of stack is maximum).
