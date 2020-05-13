

from collections import deque

#------------Iterative DFS----------------#


# def dfs(g):

# 	d = deque([0])

# 	tarvesed = set()

# 	while len(d):
# 		node = d.popleft()
# 		if node not in tarvesed:
# 			print(node, end=" ")
# 		tarvesed.add(node)

# 		for i in range(-1, -len(g[node])-1, -1):
# 			if g[node][i] not in tarvesed:
# 				d.appendleft(g[node][i])


#------------------Recursive DFS----------------#

# tarversed  = set()

# def DFS(g, start):
# 	global tarversed

# 	print(start, end=" ")
# 	tarversed.add(start)

# 	for node in g[start]:

# 		if node not in tarversed:
# 			DFS(g, node)


# DFS(graph, 1)




#---------------------BFS----------------#

# def BFS(g, start):

# 	d = deque([start])
# 	tarversed = set()

# 	while len(d):
# 		node = d.popleft()

# 		if node not in tarversed:
# 			print(node, end=" ")
# 			tarversed.add(node)

# 			for n in g[node]:
# 				d.append(n)

#   BFS(graph, 2)
#----------------Can't think of any recursive approch of BFS :-(     #








#-------------check the connectivity between two vertex in a graph----------#

# def checkConnectivity(g, v1, v2):
# 	s1 = set()
# 	s2 = set()


# 	d1 = deque([v1])
# 	while len(d1):
# 		node = d1.popleft()

# 		if node not in s1:
# 			s1.add(node)

# 			for n in g[node]:
# 				d1.append(n)


# 	d2 = deque([v2])

# 	while len(d2):
# 		node = d2.popleft()

# 		if node not in s2:
# 			s2.add(node)

# 			for n in g[node]:
# 				d2.append(n)


# 	print(s1)
# 	print(s2)

# 	print(not s1.isdisjoint(s2))

#   (checkConnectivity(graph, 1, 3))


#----------------Dijkstra Algo---------------------#


from queue import PriorityQueue

# def Dijkstra(edges, start, n):     # O(ElogV)

# 	pq = PriorityQueue()
# 	trav = [False]*n

# 	pq.put((0, start))
# 	d = {start:0}


# 	while not pq.empty():

# 		elem = pq.get()
# 		cost = elem[0]
# 		ver = elem[1]
# 		trav[ver-1] = True

# 		for edge in edges:
# 			if edge[0]==ver and not trav[edge[1]-1]:     # Consider all neighbours of ver
# 				ncost = cost+edge[2]

# 				if edge[1] in d:
# 					if ncost<d[edge[1]]:
# 						d[edge[1]] = ncost
# 						pq.put((ncost, edge[1]))
# 				else:
# 					d[edge[1]] = ncost
# 					pq.put((ncost, edge[1]))

# 	print(d)




# Dijkstra([(1,2,24), (1,3,3), (1,4,20), (3,4,12)], 1, 4)  # from v1 [0, 24, 3, 15]





#------------------------Kruskal Algo for MST-----------#
# Always select the minimum edge but make sure it does not make cycle.

# def way(edges, v1, v2):
# 	s1 = set()
# 	s2 = set()

# 	graph = {}

# 	for edg in edges:
# 		if edg[0] in graph:
# 			graph[edg[0]].append(edg[1])
# 		else:
# 			graph[edg[0]] = [edg[1]]

# 		if edg[1] in graph:
# 			graph[edg[1]].append(edg[0])
# 		else:
# 			graph[edg[1]] = [edg[0]]


# 	if v1 not in graph or v2 not in graph:
# 		return False


# 	d1 = deque()
# 	d1.append(v1)
# 	d2 = deque()
# 	d2.append(v2)

# 	while len(d1):
# 		node = d1.popleft()

# 		s1.add(node)

# 		for ver in graph[node]:
# 			if ver not in s1:
# 				d1.append(ver)



# 	while len(d2):
# 		node = d2.popleft()

# 		s2.add(node)

# 		for ver in graph[node]:
# 			if ver not in s2:
# 				d2.append(ver)


# 	return (not s1.isdisjoint(s2))






# def kruskals(edges, n):

# 	pq  = PriorityQueue()

# 	for edg in edges:
# 		pq.put((edg[2], (edg[0], edg[1])))



# 	selEdges = []
# 	mincost = 0

# 	while not pq.empty():

# 		edg = pq.get()


# 		if way(selEdges, edg[1][0], edg[1][1]):     #Check if already a way, so to not form cycle
# 			pass
# 		else:
# 			selEdges.append((edg[1][0], edg[1][1]))
# 			mincost += edg[0]

# 	return (selEdges, mincost)


# print(kruskals([(0,1,10), (0,2,6), (0,3,5), (2,3,4), (1,3,15)], 4))













#-------------------Prims Alogorithm---------------#
# Always select the minimmum cost connected edge

# def Prims(edges, n):

# 	edgesUsed = set()
# 	cost = 0

# 	nodes = set()


# 	pq = PriorityQueue()
# 	for edge in edges:
# 		pq.put((edge[2], (edge[0], edge[1])))


# 	while not pq.empty():

# 		skippedElems = []

# 		while not pq.empty():

# 			elem = pq.get()
# 			edge = elem[1]

# 			if len(nodes)==0:
# 				nodes.add(edge[0])
# 				nodes.add(edge[1])
# 				edgesUsed.add(edge)
# 				cost+=elem[0]
# 				break

# 			elif (edge[0] in nodes and edge[1] not in nodes):
# 				nodes.add(edge[1])
# 				edgesUsed.add(edge)
# 				cost+=elem[0]
# 				break

# 			elif (edge[0] not in nodes and edge[1] in nodes):
# 				nodes.add(edge[0])
# 				edgesUsed.add(edge)
# 				cost+=elem[0]
# 				break

# 			else:
# 				skippedElems.append(elem)

# 		if len(nodes)==n:
# 			break
# 		for elem in skippedElems:
# 			pq.put((elem[0], elem[1]))


# 	print(edgesUsed)
# 	print(cost)
# 	return

# Prims([(0,1,10), (0,2,6), (2,3,4), (0,3,5), (1,3,15)], 4)









#----------------------Bellman's ford Algo-----------------------#
# Works well for negative cost edge.




# def BellmanFord(edges, n):    O(EV)
#
#     dis = [float('inf')]*(n+1)
#     dis[1] = 0
#     for i in range(n-1):   # at most v-1 times.
#         update = False
#         for edge in edges:          # Iterate through every edge and relax the distance if possible.
#             if dis[edge[0]]+edge[2] < dis[edge[1]]:
#                 dis[edge[1]] = dis[edge[0]]+edge[2]
#                 update = True
#         if not update:
#             return dis
#
#     return dis


# BellmanFord([(1,2,24), (1,3,3), (1,4,20), (3,4,12)], 4)  # from v1 [0, 24, 3, 15]







#--------------------------Floyd Warshall Algorithm-------------------------#
# TO find the shortest path between all pair of vertices.


# def FloydWarshall(mat, n):

# 	for row in mat:
# 		print(*row)

# 	for Mid in range(n):
# 		for i in range(n):
# 			for j in range(n):
# 				if mat[i][Mid]!=None and mat[Mid][j]!=None:
# 					cost = mat[i][Mid]+mat[Mid][j]
# 					if mat[i][j]!=None:
# 						if cost<mat[i][j]:
# 							mat[i][j] = cost
# 					else:
# 						mat[i][j] = cost

# 	print()
# 	print()
# 	for row in mat:
# 		print(*row)

# 	return

# FloydWarshall([[0,3,None,7], [8,0,2,None], [5,None,0,1], [2,None,None,0]], 4)







# Bridges/cut edges and Articulation points/cut vertex

# Calculate low-link values for every node.
# bridge is where  ===>   id(e.from) < low-link-value(e.to)

#low-link value of a node is defined as the smallest id reachable from the node (including itself). #(O(V.(V+E)))
