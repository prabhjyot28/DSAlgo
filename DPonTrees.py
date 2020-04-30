TYPE 1
# Calculate the max sum path from root to leaves
# Calculate height of a tree.

def DFS(root):
    if not root:
        return 0

    ans = 0
    for n in root.children:
        ans = max(ans, root.val+DFS(n))
    return ans


TYPE 2  (In-Out DP)
# Diameter of tree for each node as root,  in O(n)
# For every node calculate sum of distances of that node to every other node., in O(n)   (leetcode 834)



TYPE 3  (Binary Lipting)  / (Fenwick Tree / BIT)
# Lowest Common ancestor of two nodes in (logn)
