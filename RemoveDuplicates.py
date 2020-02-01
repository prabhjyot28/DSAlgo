# This function should return duplicates from a sorted array (inplace) and return the 
# length of new array  in O(n)


def removeDuplicates(arr):
	start = 0

	for i in range(1, len(arr)):
		if arr[i] == arr[start]:
			pass
		else:
			start+=1
			arr[start] = arr[i]

	return start+1



arr = [0,0,1,1,2,3,4,5,5, 6]
n = removeDuplicates(arr)

for i in range(n):
	print(arr[i], end=" ")






