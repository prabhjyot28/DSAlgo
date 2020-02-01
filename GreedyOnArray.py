##  Q11 is very important


# Q1 Minimum product possible of subset of any array


# def minProduct(arr):
# 	arr.sort()

# 	if arr[0]>0:
# 		return arr[0]
# 	elif arr[0]==0:
# 		return 0

# 	else:
# 		countNeg = 0
# 		for val in arr:
# 			if val<0:
# 				countNeg+=1

# 		product = arr[0]

# 		for i in range(1, len(arr)):
# 			if arr[i]!=0:
# 				product *= arr[i]


# 		if countNeg%2!=0:
# 			return product
# 		else:
# 			lastNeg = arr[0]
# 			for val in arr:
# 				if val<0:
# 					lastNeg = val
# 				else:
# 					break

# 			return int(product/lastNeg)



# print(minProduct([-1, -1, -2, 4, 3,0,1,12,33,1]))



# ---------------------------------------------------------------------------------------


#  Q2 Maximum product subset of an array

# def maximumProduct(arr):
# 	arr.sort()

# 	if arr[0]>0:
# 		product = arr[0]
# 		for i in range(1, len(arr)):
# 			product *= arr[i]

# 		return product

# 	elif arr[0]==0:

# 		for i in range(len(arr)):
# 			if arr[i]>0:
# 				product = arr[i]
# 				index = i
# 				break
# 			else:
# 				pass

# 		if not product:
# 			return 0

# 		for i in range(index+1, len(arr)):
# 			product = product*arr[i]

# 		return product

# 	else:

# 		product = arr[0]

# 		for i in range(1, len(arr)):
# 			if arr[i]!=0:
# 				product *= arr[i]


# 		negs = 0
# 		pos = 0
# 		zeros = 0
# 		for val in arr:
# 			if val<0:
# 				negs+=1
# 			elif val==0:
# 				zeros+=1
# 			else:
# 				pos+=1

		

# 		if negs%2==0:
# 			return product
# 		else:

# 			lastNeg = arr[0]

# 			for i in range(1, len(arr)):
# 				if arr[i]<0:
# 					lastNeg = arr[i]
# 				else:
# 					break

# 			if pos:
# 				return int(product/lastNeg)
# 			else:
# 				if negs==1 and zeros:
# 					return 0

# 				return product




# print(maximumProduct([-4, 0, 1, -5, 2, 1, -1 ]))




# ---------------------------------------------------------------------------------------




#  Q3 Maximize the sum of arr[i]*i

# def maximizeSum(arr):
# 	arr.sort()

# 	s = 0
# 	for i in range(len(arr)):
# 		s+= (arr[i]*i)


# 	return s

# print(maximizeSum([19, 20 ]))



# Q4 Maximum absolute sum of array elements

# def maxAbsSum(arr):
# 	from collections import deque

# 	arr.sort()

# 	d = deque(arr)

# 	out = []

# 	while len(d)>1:
# 		small = d.popleft()
# 		large = d.pop()

# 		out.append(small)
# 		out.append(large)


# 	if len(d):
# 		elem = d.pop()
# 		out.append(elem)


# 	print(out)
# 	s = abs(out[-1]-out[0])

# 	for i in range(1, len(out)):
# 		print(s)
# 		s+= abs(out[i]-out[i-1])

# 	return s


# print(maxAbsSum([1, 2, 4, 8]))



# Q5  Maximize array sum after k negations


# def maxArrSum(arr, k):    # we can optimize the code by removing sort and use
# 						  # a heap to get the minimum value out of it.
# 	arr.sort()

# 	utilize = 0

# 	for i in range(len(arr)):
# 		if arr[i]<0 and utilize<k:
# 			arr[i] = -arr[i]
# 			utilize+=1

# 	zero = 0
# 	for val in arr:
# 		if val==0:
# 			zero+=1

# 	if zero:
# 		return sum(arr)

# 	else:
# 		if utilize<k:
# 			if (utilize-k)%2==0:
# 				return sum(arr)
# 			else:
# 				small = min(arr)
# 				return (sum(arr) - 2*small)



# print(maxArrSum([9, 8, 8, 5], 3))




# Q6 Maximum sum of increasing order elements from n arrays


# this does not always gives the right solution because there may be case when right
# sum will be maximum by not selecting the largest element from last array.

# def select(arr, last):

# 	if last==None:
# 		return arr[-1]

# 	if arr[-1]<last:
# 		return arr[-1]
# 	else:
# 		for i in range(len(arr)-1, -1, -1):
# 			if arr[i]<last:
# 				return arr[i]
# 		return None



# def maximumSumNarr(arr):
# 	n = len(arr)

# 	for i in range(n):
# 		arr[i].sort()

# 	last = None
# 	s = 0
# 	for i in range(n-1, -1, -1):

# 		elem = select(arr[i], last)
# 		if elem:
# 			s+=elem
# 			last = elem
# 		else:
# 			return 0

# 	return s


# print(maximumSumNarr([[9,8,7],  
#        [6,5,4],  
#        [3,2,1]]))







#  Q7 Maximum height pyramid from given array of object



# def maxHeightPyramid(arr):
# 	arr.sort()

# 	height = 0
# 	currentWid = 0
# 	currentElems = 0

# 	while sum(arr)>currentWid and len(arr)>currentElems:

# 		nextWidth = 0
# 		nextElems = 0
# 		level = []
# 		while (nextWidth<=currentWid or nextElems<=currentElems):
# 			elem = arr.pop(0)
# 			level.append(elem)
# 			nextWidth += elem
# 			nextElems += 1

# 		print(level)
# 		currentWid = nextWidth
# 		currentElems = nextElems
# 		height+=1

# 	return height


# print(maxHeightPyramid([10, 20, 30, 50, 60, 70]))




# Q8 Divide array into two parts such that difference of their sums is maximum

# def divideAndMax(arr, k):

# 	import heapq

# 	heapq.heapify(arr)

# 	klenarr = []

# 	for i in range(k):
# 		elem = heapq.heappop(arr)
# 		klenarr.append(elem)

# 	return abs(sum(klenarr)-sum(arr))


# print(divideAndMax([1, 1, 1, 1, 1, 1, 1, 1], 3))




# Q9 Minimum sum of product of two array with k modifications on 1st array
# this is obtained by applying all modifications to only one value of array
# which makes it a greedy algo.

# def minSumProduct(arr1, arr2, k):

# 	out = []

# 	for i in range(len(arr1)):

# 		arr1[i]+= 2*k

# 		prod = [arr1[i]*arr2[i] for i in range(len(arr1))]

# 		s1 = sum(prod)

# 		arr1[i]-=4*k

# 		prod = [arr1[i]*arr2[i] for i in range(len(arr1))]
# 		s2 = sum(prod)

# 		out.append(min(s1, s2))

# 		arr1[i]+=2*k


# 	return min(out)

# print(minSumProduct([2, 3, 4, 5, 4], [3, 4, 2, 3, 2], 3))





# Q10 Minimum operations to make GCD of array a multiple of k

# def minOptoGCD(arr, k):

# 	count = 0
# 	for val in arr:
# 		if val%k==0:
# 			pass
# 		else:
# 			rem = val%k
# 			count+=min(rem, k-rem)

# 	return count


# print(minOptoGCD([4,9,6], 5))



# Q11 Minimum sum of two numbers formed from digits of an array


# def minSumOfTwo(arr):
# 	import heapq

# 	heapq.heapify(arr)

# 	first = ''
# 	second = ''

# 	while len(arr)>1:
# 		one = heapq.heappop(arr)
# 		two = heapq.heappop(arr)

# 		first+=str(one)
# 		second+=str(two)

# 	if len(arr):
# 		elem = heapq.heappop(arr)

# 		first+=str(elem)


# 	return int(first)+int(second)


# print(minSumOfTwo([5, 3, 0, 7, 4]))




# Q12 Minimum increment/decrement to make array non-Increasing

# def minChanges(arr):
# 	changes = 0

# 	for i in range(1, len(arr)):
# 		if arr[i]>arr[i-1]:
# 			if (i+1)<len(arr) and arr[i]>=arr[i+1]:
# 				changes+=arr[i]-arr[i-1]
# 				arr[i] = arr[i-1]

# 			else:
# 				changes = arr[i]-arr[i-1]
# 				arr[i-1] = arr[i]

# 	return changes

# print(minChanges([3, 1, 2, 1 ]))




# Q13 Making elements of two arrays same with minimum increment/decrement


# def makeArrElemEqual(a, b):
# 	a.sort()
# 	b.sort()

# 	changes = 0
# 	for i in range(len(a)):
# 		changes+=abs(a[i]-b[i])

# 	return changes


# print(makeArrElemEqual([3,1,1], [1,1,2]))



# Q14 Is Sorting array possible with reverse around middle.


# def IsSortingPossible(arr):
	
# 	from collections import deque

# 	d = deque(arr)

# 	while len(d)>1:
# 		small = min(d)
# 		large = max(d)

# 		if ((small==d[0] or small == d[-1]) and (large==d[0] or large == d[-1])):
# 			d.pop()
# 			d.popleft()

# 		else:
# 			return 'No'

# 	return('Yes')


# print(IsSortingPossible([1, 7, 6, 4, 5, 3, 2, 8]))


# Q15 sum of all possible maximum area rectangles 

def areaSumRectangle(arr):
	












































































