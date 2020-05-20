
# To fix imbalance we perform rotations.
# T1, T2 and T3 are subtrees of the tree rooted with y
#   (on left side) or x (on right side)
#                 y                               x
#                / \     Right Rotation          /  \
#               x   T3   – – – – – – – >        T1   y
#              / \       < - - - - - - -            / \
#             T1  T2     Left Rotation            T2  T3

class Node:
    from random import randint
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = randint(0, 100)

class Treap:
    def __init__(self):
        self.root = None


    def leftRotate(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2
        return y


    def rightRotate(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2
        return x


    def _insert(self, root, key):
        if not root:
            return Node(key)

        if key<=root.key:
            root.left = self._insert(root.left, key)
            if root.left.p > root.p:
                root = self.rightRotate(root)
        else:
            root.right = self._insert(root.right, key)
            if root.right.p>root.p:
                root = self.leftRotate(root)
        return root

    def _delete(self, root, key):
        if root==None:
            return root

        if key<root.key:
            root.left = self._delete(root.left, key)
        elif key>root.key:
            root.right = self._delete(root.right, key)

        elif root.left == None:
            temp = root.right
            del root
            root = temp
        elif root.right == None:
            temp = root.left
            del root
            root = temp
        elif root.left.p<root.right.p:
            root = self.leftRotate(root)
            root.left = self._delete(root.left, key)
        else:
            root = self.rightRotate(root)
            root.right = self._delete(root.right, key)
        return root


    def insert(self, key):
        self.root = self._insert(self.root, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)



treap = Treap()
treap.insert(1)
treap.insert(2)
treap.insert(4)
treap.insert(3)
treap.insert(9)
treap.insert(6)
treap.delete(4)
