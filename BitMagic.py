# Print binary reps

# def binary(num):                           #O(log n)
# 	val = ''

# 	while num:
# 		val = str(num&1)+ val
# 		num = num>>1

# 	print(val)


# def binary(num):
# 	print(bin(13))

# binary(13)




#--------Check even/odd------------#
# def checkEvenOdd(num):
# 	if num & 1:
# 		print('Odd')
# 	else:
# 		print('Even')

# 	return

# checkEvenOdd(178)


# Counting set bits


# def countSetBits(num):               #O(log n)

# 	count = 0

# 	while num:
# 		if num&1:
# 			count+=1

# 		num= num>>1

# 	print(count)




#------------------Brian Kernighan' Algo-------------#
# subtracting 1 from a number flips all the bits after the rightmost set bit (including it)

# eg.
# 10   ==>   1010
# 9    ==>   1001
# 8    ==>   1000
# 7    ==>   0111

# Get the last set bits
# lastsetbit = n & ~(n-1)
# lastsetbit = n&-n     (~(n-1) == -(n-1)-1)



# def countSetBits(num):				#O(log n)

# 	count = 0
# 	while num:
# 		count+=1
# 		num = num&num-1

# 	print(count)


# countSetBits(6)




#-------Missing number in an array of (1-n)-----------#

# def missingNum(arr, n):
# 	val = 0
#     for v in arr:
#         val = val^v

#     for i in range(1, n+1):
#         val = val^i

#     return val



#--------------check number is power of 8----------#

# from math import log2
# def check(num):
# 	if log2(num)%3==0:
# 		print('Yes {} is power of 8'.format(num))
# 	else:
# 		print('No {} is not a power of 8'.format(num))


# check(64)


# Similary we can do for power of 2, 4, 16, 32




# ---------------Check if number if power of 2-------------------#
# If a number if power of 2 then its binary representation there will only be one set bit.
# so if (x & x-1)==0 that means number is power of 2.





#--------------check number is multiple of 3-------------#
# Every pow(2, x) can be represent by multiple of 3k+1 or 3k-1.
# 3k+1 for even places and 3k-1 for odd places.
# so, abs(evensetbits - oddsetbits)%3 decide number is divisible by 3 or not.


# def check(num):
# 	evensetbits = 0
# 	oddsetbits = 0

# 	bn = bin(num)
# 	bn = bn.split('b')[1]

# 	for i in range(len(bn)):
# 		if i%2==0 and bn[i]=='1':
# 			evensetbits+=1
# 		if i%2!=0 and bn[i]=='1':
# 			oddsetbits+=1

# 	if abs(evensetbits-oddsetbits)%3==0:
# 		return True
# 	else:
# 		return False
