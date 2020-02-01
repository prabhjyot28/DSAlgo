#  Q1  Binary Search (Recursive approch)

# def binarySearch(arr, key, start, end):

# 	mid = (start+end)//2

# 	if start>end:
# 		print('Not found')
# 		return

# 	if arr[mid] == key:
# 		print(mid)
# 		return

# 	else:

# 		if key>arr[mid]:
# 			binarySearch(arr, key, mid+1, end)
# 		else:
# 			binarySearch(arr, key, start, mid-1)

# 		return



# def Search(arr, key):
# 	end = len(arr)-1
# 	binarySearch(arr, key, 0, end)


# Search([1,2,3,4,5,9,15,20], 15)

#------------------------------------------------------------------------------------

# def binarySearch(arr, key):       # (Iterative approch)
	
# 	start = 0
# 	end = len(arr)-1


# 	while(start<=end):
# 		mid = (start+end)//2

# 		if arr[mid]==key:
# 			print(mid)
# 			return

# 		else:

# 			if key>arr[mid]:
# 				start = mid+1
# 			else:
# 				end = mid-1

# 	print('Not found')
# 	return



# binarySearch([1,2,3,4,5,9,15,20], 15)






#  Q2 Merge Sort Algorithm


# def merge(arr1, arr2):                    # 2-way merging for 2 sorted arrays into one
# 	arr = []

# 	i = 0
# 	j = 0

# 	while(i<len(arr1) and j<len(arr2)):
# 		if arr1[i]<arr2[j]:
# 			arr.append(arr1[i])
# 			i+=1
# 		else:
# 			arr.append(arr2[j])
# 			j+=1

# 	while(i<len(arr1)):
# 		arr.append(arr1[i])
# 		i+=1

# 	while(j<len(arr2)):
# 		arr.append(arr2[j])
# 		j+=1

# 	return arr




# def mergeSort(arr):
# 	if len(arr)==1:
# 		return arr

# 	mid = len(arr)//2
# 	arr1 = arr[:mid]
# 	arr2 = arr[mid:]

# 	return merge(mergeSort(arr1), mergeSort(arr2))




# print(mergeSort([2,1,8,4,55, 0, -1, 9,4,3]))




#  Q3 Qucik sort
#  The idea behind quick sort is that we call an element in a list os sorted if all
#  elements before it is smaller than it and all elements after it is greater than it.



# def QuickSort(arr):

# 	if(len(arr)==0):
# 		return []

# 	if len(arr)==1:
# 		return arr

# 	pivot = arr[0]
# 	smaller = []
# 	equal = []
# 	larger = []

# 	for i in range(len(arr)):
# 		if arr[i]<pivot:
# 			smaller.append(arr[i])
# 		elif arr[i]==pivot:
# 			equal.append(arr[i])
# 		else:
# 			larger.append(arr[i])


# 	return QuickSort(smaller)+equal+QuickSort(larger)



# print(QuickSort([2,1,8,4,55, 0, -1, 9,4,3]))

# ---------------------------------------------------------------------

# INPLACE QUICK SORT

# def partitioning(arr, start, end):             #Inplace partitioning across pivot arr[0]
	
# 	pivot = arr[start]
# 	ifl = None
# 	ifr = None

# 	while(True):
# 		for i in range(start+1, end+1):
# 			if arr[i]>pivot:
# 				ifl = i
# 				break

# 		for j in range(end, start, -1):
# 			if arr[j]<=pivot:
# 				ifr = j
# 				break

# 		if not ifl or not ifr:
# 			break

# 		if ifl>ifr:
# 			break
# 		else:
# 			arr[ifl], arr[ifr] = arr[ifr], arr[ifl]

# 	if not ifl:
# 		arr[start], arr[end] = arr[end], arr[start]
# 		return end


# 	if not ifr:
# 		return start

# 	arr[start], arr[ifr] = arr[ifr], arr[start]

# 	return ifr




# def QuickSortHelper(arr, start, end):
# 	if end<=start:
# 		return

# 	pivotIndex = partitioning(arr, start, end)

# 	QuickSortHelper(arr, start, pivotIndex-1)
# 	QuickSortHelper(arr, pivotIndex+1, end)

# 	return arr




# def QuickSort(arr):
# 	start = 0
# 	end = len(arr)-1
	
# 	return QuickSortHelper(arr, start, end)



# arr = [1,0,-1,2,3,-1,44,9,7,81]
# print(QuickSort(arr))





# Q5 Strassens Matrix Multiplication
# use 3 for loops O(n**3) rather than strassens divide and conquer approch O(n**2.8)
# plus it takes extra stack space for recurssive function.


















