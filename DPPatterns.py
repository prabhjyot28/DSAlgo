
# https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns

# fib ----

ans = [0, 1]
for i in range(2, n+1):
	ans.append(ans[i-1]+ans[i-2])


# LIS ----

ans = []
for i in range(len(arr)):
	ans.append(1)
	for j in range(i):
		if(.....):
			ans[i] = max(ans[i], ans[j]+1)



#using binary search

sub = []
from bisect import bisect_left
for val in arr:
	ind = bisect_left(sub, val)
	if ind==len(sub):
		sub.append(val)
	else:
		sub[ind] = val


# sort by one parameter and apply binary search dp on another

pairs.sort(key = lambda x: x[0], -x[1])
#so that while applying dp on 2nd para, we should not double count pairs like ([3,3] and [3,4]) incase only one can consider



# LCS------------------------------------------------

# top - down (memoization) is easy to think

dp = [[0,0], [0, 0], [0, 0]]   #2d dp initialised with 0.
for i in range(len(s1)):
	for j in range(len(s2)):
		dp[i][j] = ............



# LPS ------------------------------------------------

dp = [[]]    # 2d dp table, dp[i][j] represents LPS from [i, j]
# So, we not need to calculate where j<i (useless).

for i in range(len(arr)):
	dp[i][i] = 1

# values should be filled diagonally.
for c in range(1, len(arr)):
	for r in range(len(arr)-c):
		col = r+c
		dp[r][col] = .......


# 0/1 Knapsack (Repeation or with out repetition)  --------------------------

dp = [[]]  # 2d table for i&b 0<=i<n and 0<=b<=B.
#O(nB) (its not a polynomial runtime in input size), cause to represent B we just required logB space (no of bits)
# So our running time is exponential to input size (nlogB), and it's not a polynomial time algorithm (IMPORTANT).
#dp[i][b] means max value achievable using a subset of objects [1,..i] and total weights<=b.

#Table is filled row by row.
for i in range(n+1):
	for b in range(B+1):
		dp[i][b] = .........

#Coin change, Subset sum problem also follows the same pattern.


#Knapsack with repetition can be solved using 1D table (0<=b<=B).





# Matrix Chain --------------------------

dp= [[]]  # 2d dp table in i, j where dp[i][j] representing min. cost of multiplying matrixes from [Ai....Aj].
# table is filled diagonnally similar to LPS.



# SHORTEST PATH ALGORITHMS USING DP-------------------

dp = [[]]  #DP[i][z] represents length of shortest path from from source to z, using <=i edges.
# 0<=i<=n-1 (edges in the graph),  z<=v (vertices in the graph).
