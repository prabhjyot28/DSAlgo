
# Q1 Ugly Numbers

# def nthUgly(n):     # Numbers which are multiple of 2,3,5 only
# 	two = 0
# 	three = 0
# 	five = 0

# 	nos = [1]

# 	for i in range(n-1):
# 		num = min(nos[two]*2, nos[three]*3, nos[five]*5)

# 		if num==nos[two]*2:
# 			two+=1

# 		if num==nos[three]*3:
# 			three += 1

# 		if num==nos[five]*5:
# 			five+=1


# 		nos.append(num)


	
# 	return nos[n-1]



# print(nthUgly(150))






# Q2 Fibbonaci Series

# def fibonaci(n, f={}):
# 	if n<=1:
# 		return n

# 	if n in f:
# 		return f[n]

# 	else:
# 		f[n] = fibonaci(n-1, f)+fibonaci(n-2, f)
# 		return f[n]

# print(fibonaci(9))


#------------------Using iteration----------------#


# def fibonaci(n):
# 	f = [0, 1]

# 	for i in range(2,n+1):
# 		f.append(f[i-1]+f[i-2])


# 	print(f)
# 	return f[n]

# print(fibonaci(9))




# Q3 Maximum Subarray Sum problem

# Naive Sol (brute force) taken O(n**2) Dp solves it in O(n) only.


#-----------Using Dp (Kaden's Algorithm) O(n) ----------------#

# def maxSumSubarr(arr):
# 	sums = []

# 	last = 0
# 	for val in arr:
# 		maxSub = max(val, last+val)
# 		last = maxSub
# 		sums.append(last)

# 	return max(sums)

# print(maxSumSubarr([-2,3,1,-7,3,2,-1]))



# Q4 Egg Dropping problem

# f(n, e) = min of all x=1 to x=n-1 ( max(f(n-x, e), f(x-1, e-1))+1 )

# cache = {}

# def dropEggs(n, e):
# 	global cache

# 	if n==1:
# 		return 1

# 	if n==0:
# 		return 0

# 	if e==1:
# 		return n

# 	res = 11111111111111111111

# 	for i in range(1, n+1):
# 		if (n-i, e) in cache:
# 			a = cache[(n-i, e)]
# 		else:
# 			cache[(n-i, e)] = dropEggs(n-i, e)
# 			a = cache[(n-i, e)]

# 		if (i-1, e-1) in cache:
# 			b = cache[(i-1, e-1)]
# 		else:
# 			cache[(i-1, e-1)] = dropEggs(i-1, e-1)
# 			b = cache[(i-1, e-1)]

# 		subres = max(a, b)+1

# 		if subres<res:
# 			res = subres

# 	return res


# print(dropEggs(9,3))
# print(len(cache.keys()))



#-------------------- Using bottom approch (iterative formula)-------------#


# def dropEggs(n, e):

# 	arr = [[0 for j in range(n+1)] for i in range(e+1)]

# 	for i in range(1, len(arr[1])):
# 		arr[1][i] = i

# 	for i in range(1, len(arr)):
# 		arr[i][1] = 1


# 	for i in range(2, e+1):
# 		for j in range(2, k+1):

# 			arr[i][j]  = 1111111111111111
# 			# Complete rest of part




# 	for l in arr:
# 		print(*l)


# dropEggs(9, 3)





# Q5 longest common subsequence

# NOTE:  A subsequence does not need to be contiguos but subarray is always contiguos.


#------------------Using recursion--------------#


# cache = {}
# def lcs(a, b):

# 	if a==b:
# 		return len(a)

# 	if len(a)==0 or len(b)==0:
# 		return 0

# 	if a[-1]==b[-1]:
# 		s = frozenset((a[:-1], b[:-1]))

# 		if s in cache:
# 			return 1+cache[s]
# 		else:
# 			val = lcs(a[:-1], b[:-1])
# 			cache[s] = val
# 			return 1+cache[s]

# 	else:
# 		s1 = frozenset((a, b[:-1]))
# 		s2 = frozenset((a[:-1], b))

# 		if s1 in cache:
# 			val1 = cache[s1]
# 		else:
# 			val1 = lcs(a, b[:-1])
# 			cache[s1] = val1

# 		if s2 in cache:
# 			val2 = cache[s2]
# 		else:
# 			val2 = lcs(a[:-1], b)
# 			cache[s2] = val2

# 		return max(val1, val2)



# print(lcs('aggtab', 'gxtxayb'))
# print(len(cache.keys()))




#  Q6 Range Sum Querying (Use sum array for caching)  (easy problem)

# Q7 Max Sum Rectangle in a 2D Matrix


# ---------------Using brute force approch-----------#

# def maxSumRectangle(arr):

# 	res = 0
# 	rows = len(arr)
# 	cols = len(arr[0])

# 	for i in range(rows):
# 		for j in range(cols):

# 			topLeft = (i, j)

# 			for k in range(i, rows):
# 				for l in range(j, cols):

# 					bottomRight = (k, l)

# 					s = 0
# 					for r in range(i, k+1):
# 						for c in range(j, l+1):

# 							s+=arr[r][c]

# 					if s > res:
# 						res = s

# 	print(res)



#----------------------------Using DP--------------------------#

# def maxSumRectangle(arr):

# 	rows = len(arr)
# 	cols = len(arr[0])

# 	sums = [0 for i in range(rows)]
# 	res = 0

# 	for L in range(cols):
# 		for R in range(L, cols):

# 			for i in range(rows):
# 				s = 0
# 				for j in range(L, R+1):
# 					s+=arr[i][j]

# 				sums[i] = s

# 			#------Applying Kaden's on sums array-----#

# 			sumOfSums = []
# 			last = 0
# 			for val in sums:
# 				s = max(val, last+val)
# 				sumOfSums.append(s)
# 				last = s

# 			subres = max(sumOfSums)

# 			if subres>res:
# 				res = subres

# 	print(res)



# maxSumRectangle([[6,-5,-7,4,-4], [-9, 3, -6, 5, 2], [-10, 4, 7, -6, 3], [-8, 9, -3, 3, -7]])



# Q8 Total unique ways to make a coin change
# Order of coin does not matter we need to find combinations



# cache = {}
# def coinChange(coins, change):
# 	global cache

# 	if change==0:
# 		return 1

# 	if len(coins)==0 and change>0:
# 		return 0

# 	if len(coins)<0:
# 		return 0

# 	if change<0:
# 		return 0


# 	if (tuple(coins), change-coins[-1]) in cache:
# 		a = cache[(tuple(coins), change-coins[-1])]
# 	else:
# 		cache[(tuple(coins), change-coins[-1])] = coinChange(coins, change-coins[-1])
# 		a = cache[(tuple(coins), change-coins[-1])]

# 	if (tuple(coins[:-1]), change) in cache:
# 		b = cache[(tuple(coins[:-1]), change)]
# 	else:
# 		cache[(tuple(coins[:-1]), change)] = coinChange(coins[:-1], change)
# 		b = cache[(tuple(coins[:-1]), change)]



# 	return  a+b

	


# print(coinChange([1,2,5], 5))




# Q9 Climbing staircase

# Problem is to find no of ways we can climb up to particular stair and 
# we are only allowed to make 1 or 2 move.

# cache = {}
# def climbStair(n):
# 	global cache


# 	if n==1:
# 		return 1
# 	if n==2:
# 		return 2

# 	if n-1 in cache:
# 		a = cache[n-1]
# 	else:
# 		cache[n-1] = climbStair(n-1)
# 		a = cache[n-1]

# 	if n-2 in cache:
# 		b = cache[n-2]
# 	else:
# 		cache[n-2] = climbStair(n-2)
# 		b = cache[n-2]

# 	return a+b


# print(climbStair(5))




# Q10  count total unique binary search trees / nth catalan number
#  (Total BT = Total BST * n!)
#  Total BST = Catalan Number = 2nCn / n+1   =  ((2n)! / ((n+1)!*n!))




# cache = {}
# def countBST(n):
# 	global cache

# 	if n<0: 
# 		return 0

# 	if n==0:
# 		return 1

# 	if n==1:
# 		return 1

# 	if n==2:
# 		return 2


# 	count = 0
# 	for i in range(1, n+1):

# 		if (n-i) in cache:
# 			a = cache[n-i]
# 		else:
# 			cache[n-i] = countBST(n-i)
# 			a = cache[n-i]

# 		if (i-1) in cache:
# 			b = cache[i-1]
# 		else:
# 			cache[i-1] = countBST(i-1)
# 			b = cache[i-1]


# 		count += a*b

# 	return count




# print(countBST(5))


# Applications of Catalan number

# Number of expressions containing n pairs of paranthesis
# Number of BST with n keys 
# Number of full binary trees with n+1 leaves



# Q11 Minimum coins needed to make an amount of change
 
# cache = {}
# def minCoins(coins, val):
# 	global cache

# 	if val in coins:
# 		return 1


# 	if val<min(coins):
# 		return None


# 	res = 11111111111

# 	for i in range(len(coins)):

# 		if val-coins[i] in cache:
# 			used = cache[val-coins[i]]

# 		else:
# 			cache[val-coins[i]] = minCoins(coins, val-coins[i])
# 			used = cache[val-coins[i]]

# 		if used and used+1<res:
# 			res = used+1

# 	return res



# print(minCoins([1, 2, 5], 11))


# Q12 Total ways to decode a string (1-9)

# ways = 0
# def decodeString(s, sel = []):
# 	global ways

# 	if not len(s):
# 		ways+=1
# 		return

	
# 	for i in range(1, len(s)+1):
# 		c = s[:i]

# 		sel.append(c)

# 		if int(c)<=26:
# 			decodeString(s[i:], sel)
# 		else:
# 			break

# 		sel.pop()

# 	return



# decodeString('1236')
# print(ways)





# Q13  Levenshtein distance (Min opertaions required to convert a string into another)
# Delete, Replace, Insert operations are allowed only


# Calculate min ops required to convert string a to b.

# def minOps(a, b):

# 	if a==b:
# 		return 0

# 	if len(a)==0:
# 		return len(b)

# 	if len(b)==0:
# 		return len(a)


# 	if a[-1]==b[-1]:
# 		return minOps(a[:-1], b[:-1])

# 	else:
# 		r = minOps(a[:-1], b[:-1])+1    #replace
# 		i = minOps(a, b[:-1]) + 1		#insert
# 		d = minOps(a[:-1], b) + 1		#delete

# 		return min(r, i, d)


# print(minOps('benyam', 'ephrem'))





#  Q14 Divide an array into k parts of equal sums

# def divideArray(arr, k):





# Q15  0/1 Knapsack problem

# cache = {}
# timeSaved = 0
# def zeroOne(w, v, weight):
# 	global cache
# 	global timeSaved

# 	if not w:
# 		return 0

# 	if weight<min(w):
# 		return 0



# 	if w[-1]>weight:
# 		if (frozenset(w[:-1]), frozenset(v[:-1]), weight) in cache:
# 			timeSaved+=1
# 			return cache[(frozenset(w[:-1]), frozenset(v[:-1]), weight)]
# 		else:
# 			cache[(frozenset(w[:-1]), frozenset(v[:-1]), weight)] = zeroOne(w[:-1], v[:-1], weight)
# 			return cache[(frozenset(w[:-1]), frozenset(v[:-1]), weight)]

	

# 	if (frozenset(w[:-1]), frozenset(v[:-1]), weight) in cache:
# 		timeSaved+=1
# 		byNotIncluding = cache[(frozenset(w[:-1]), frozenset(v[:-1]), weight)]
# 	else:
# 		cache[(frozenset(w[:-1]), frozenset(v[:-1]), weight)] = zeroOne(w[:-1], v[:-1], weight)
# 		byNotIncluding = cache[(frozenset(w[:-1]), frozenset(v[:-1]), weight)]

# 	if (frozenset(w[:-1]), frozenset(v[:-1]), weight-w[-1]) in cache:
# 		timeSaved+=1
# 		byIncluding = cache[(frozenset(w[:-1]), frozenset(v[:-1]), weight-w[-1])]+v[-1]
# 	else:
# 		cache[(frozenset(w[:-1]), frozenset(v[:-1]), weight-w[-1])] = zeroOne(w[:-1], v[:-1], weight-w[-1])
# 		byIncluding = cache[(frozenset(w[:-1]), frozenset(v[:-1]), weight-w[-1])] + v[-1]


# 	return max(byIncluding, byNotIncluding)



# print(zeroOne([10, 20, 30], [60, 100, 120], 50))
# print(timeSaved)



# Q16 longest increasing subsequence












































































































































