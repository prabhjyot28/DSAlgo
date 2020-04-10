
class UnionFind:
    def __init__(self):
        self.id = {}
        self.sz = {}
        self.count = 0
        return

    def add(self, p):
        self.id[p] = p
        self.sz[p] = 1
        self.count += 1

    def root(self, i):
        node = i
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]

        # Path Compression.
        # while node!=i:
        #     next = self.id[node]
        #     self.id[node] = i
        #     node = next

        return i

    def unite(self, p, q):
        i, j = self.root(p), self.root(q)
        if i == j:
            return
        if self.sz[i] > self.sz[j]:
            i, j = j, i
        self.id[i] = j
        self.sz[j] += self.sz[i]
        self.count -= 1


# Number of components equals to number of unique roots.
