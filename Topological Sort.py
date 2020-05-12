# A Topological oredering is the oredering of nodes in a directed graph where for each directed edge between
# from node A to node B, node A appears before node B in the oredering.

# Note - Topological sorts are not unique, there are multiple valid ways.
# NOte - A graph which contains a cycle can't have a valid Topological oredering.
# Note -  The only type of graph which has a valid Topological ordering is a directed Acyclic graph (DAG).
# DAG - graphs with directed edges and no cycles. eg. Trees

# Note - For tress PreOrder traversals will give us the correct Topological order.



# STEPS TO FIND TOPOLOGICAL SORT OF ANY DAG.   (DFS Approch)  O(V+E)
# - Pick any unvisited node.
# - Do DFS from this node, while backtracking put that node in the TOPOLOGICAL sort array in reverse oredering.
# - Repeat Until there is no more unvisited nodes left.



# BFS (Approch)  O(V+E)  Since in each step every vertex will become source only once and each edge will be removed or accessed once.

Source - No incoming edge only outgoing edge.
Sink  - No outgoing edge only incoming edge.

a. Initialization
We will store the graph in Adjacency Lists, which means each parent vertex will have a list containing all of its children. We will do this using a HashMap where the ‘key’ will be the parent vertex number and the value will be a List containing children vertices.
To find the sources, we will keep a HashMap to count the in-degrees i.e., count of incoming edges of each vertex. Any vertex with ‘0’ in-degree will be a source.

b. Build the graph and find in-degrees of all vertices
We will build the graph from the input and populate the in-degrees HashMap.

c. Find all sources
All vertices with ‘0’ in-degrees will be our sources and we will store them in a Queue.

d. Sort
- For each source, do the following things:
- Add it to the sorted list.
- Get all of its children from the graph.
- Decrement the in-degree of each child by 1.
- If a child’s in-degree becomes ‘0’, add it to the sources Queue.
- Repeat step 1, until the source Queue is empty.


# THE BFS Approch can be used to find any cycle in a directed graph as if length of TOPOLOGICAL sort!= Number of vertices.
