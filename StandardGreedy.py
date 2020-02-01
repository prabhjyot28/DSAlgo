

#An optimization problem can be solved using Greedy if the problem has the following 
#property: At every step, we can make a choice that looks best at the moment, 
#and we get the optimal solution of the complete problem.



# Q1 Activity Selection problem 

# def activitySelection(S, F):
# 	data  = list(zip(S, F))

# 	d = {}

# 	for i in range(len(data)):
# 		d[data[i]] = i+1

# 	data.sort(key = lambda x: x[1])

# 	print(data)
# 	count = 1
# 	finishTime = data[0][1]
# 	for i in range(1, len(data)):
# 		if data[i][0]>=finishTime:
# 			count+=1
# 			finishTime = data[i][1]

# 	return count


# print(activitySelection([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))




# Q2 Egyptian fraction problem

#  Q3 Job sequencing 

# def jobSequencing(jd):
# 	jd.sort(key = lambda x: [-x[2]])

# 	order = [None for i in range(len(jd))]

# 	for i in range(len(jd)):

# 		index = (jd[i][1]-1)

# 		while index>=0:
# 			if order[index]==None:
# 				order[index] = jd[i]
# 				break
# 			else:
# 				index-=1

# 	totalProfit = 0
# 	for val in order:
# 		if val!=None:
# 			print(val, end=" ")
# 			totalProfit+=val[2]

# 	return totalProfit

# print(jobSequencing([('a',2,100), ('b',1,19), ('c',2,27), ('d',1,25), ('e', 3,15)]))




#  Q4 Job Sequencing Problem – Loss Minimization
# Its just like fractional knapsack problem we have to sort in the ratio of loss and time


# def lossMinimize(L, T):
# 	d= {}

# 	for i in range(len(L)):
# 		d[(L[i], T[i])] = i+1

# 	data = []

# 	for i in range(len(L)):
# 		data.append([L[i], T[i]])
# 		data[-1].append(L[i]/T[i])


# 	data.sort(key = lambda x: (-x[2]))

# 	for val in data:
# 		print(d[(val[0], val[1])], end=" ")

# 	return

# lossMinimize([3, 1, 2, 4], [4, 1000, 2, 5])




























