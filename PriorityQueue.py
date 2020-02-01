

from queue import PriorityQueue

q = PriorityQueue()

q.put((3,'rahul'))                     # enqueue in O(logN)
q.put((1,'prabhjyot'))
q.put((0,'piyush'))



while not q.empty():
	elem = q.get()
	print(elem[0])
	print(elem[1])
							# # dequeue in O(logN)



# # Deque in python, internally is built using a doubly linked list

# from collections import deque

# d = deque([1,3,3,45,5])

# d.append(100)            #O(1)
# d.appendleft(100)            #O(1)


# d.pop()            #O(1)
# d.popleft()            #O(1)



# d.index(elem, beg, end)            #O(n)

# d.insert(i, val)            #O(n)

# d.remove(val)    # first occurence            #O(n)

# d.rotate(k)      # O(k)

# d.count(val)    #O(n)

# del d[5]      #O(n)








# Heaps in python python has built in min-heap


# import heapq

# h = []

# heapq.heappush(h, 10)    # O(log n)
# heapq.heappop(h)         # O(log n)

# smallest = h[0]   # to acess smallest item without popping

# heapq.heappushpop(h, 15)   # first push then pop  
# heapq.heapreplace(h, 20)   # first pop then push


# arr = [1,2,3,4]

# heapq.heapify(arr)        # convert an array into heap in O(n)   (inplace)


# # Heapify O(n) is better than adding n items into empty heap  O(nlogn)

# heapq.nsmallest(n, arr, key=None)
# heapq.nlargest(n, arr, key = None)


# # removing ith element from heap    O(logn)

# h[i]  = h[-1]
# h.pop()

# if i<len(h):
# 	heapq._siftup(h, i)
# 	heapq._siftdown(h, 0, i)

#========================MAX HEAP========================

#heapq._heapify_max(arr)
#heapq._heappush_max(arr, val)

