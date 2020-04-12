# A Topological oredering is the oredering of nodes in a directed graph where for each directed edge between
# from node A to node B, node A appears before node B in the oredering.

# Note - Topological sorts are not unique, there are multiple valid ways.
# NOte - A graph which contains a cycle can't have a valid Topological oredering.
# Note -  The only type of graph which has a valid Topological ordering is a directed Acyclic graph (DAG).
# DAG - graphs with directed edges and no cycles. eg. Trees

# Note - For tress PreOrder traversals will give us the correct Topological order.



# STEPS TO FIND TOPOLOGICAL SORT OF ANY DAG.
# - Pick any unvisited node.
# - Do DFS from this node, while backtracking put that node in the TOPOLOGICAL sort array in reverse oredering.
# - Repeat Until there is no more unvisited nodes left.
