# BIT is useful in performing range queries for sum, product, xor etc. (not for min/max)

class BIT:
    """Implementation of a Binary Indexed Tree (Fennwick Tree)"""
    
    #def __init__(self, list):
    #    """Initialize BIT with list in O(n*log(n))"""
    #    self.array = [0] * (len(list) + 1)
    #    for idx, val in enumerate(list):
    #        self.update(idx, val)

    def __init__(self, list):
        """"Initialize BIT with list in O(n)"""
        self.array = [0] + list
        for idx in range(1, len(self.array)):
            idx2 = idx + (idx & -idx)
            if idx2 < len(self.array):
                self.array[idx2] += self.array[idx]

    def prefix_query(self, idx):
        """Computes prefix sum of up to including the idx-th element"""
        idx += 1
        result = 0
        while idx:
            result += self.array[idx]
            idx -= idx & -idx                                  #Subtracting the last bit
        return result

    def range_query(self, from_idx, to_idx):
        """Computes the range sum between two indices (both inclusive)"""
        return self.prefix_query(to_idx) - self.prefix_query(from_idx - 1)

    def update(self, idx, add):
        """Add a value to the idx-th element"""
        idx += 1
        while idx < len(self.array):
            self.array[idx] += add
            idx += idx & -idx                                  #Adding the last bit









# Segment Tree works well in performiong any range query Min, Max, Sum, Xor etc.


class SegmentTree:
    def __init__(self, values):
        self.data = [0 for _ in values] + values
        self.n = len(values)
        
        for idx in reversed(range(1, self.n)):
            self.data[idx] = min(self.data[2*idx], self.data[2*idx+1])

    def update(self, idx, value):
        idx += self.n
        self.data[idx] = value

        while idx > 0:
            idx //= 2
            self.data[idx] = min(self.data[2*idx], self.data[2*idx+1])

    def minimum(self, left, right):                             #Gives min from [left, right)
        left += self.n
        right += self.n
        minimum = self.data[left]

        while left < right:
            if left % 2:
                minimum = min(minimum, self.data[left])
                left += 1
            if right % 2:
                right -= 1                                #Because right is exclusive.
                minimum = min(minimum, self.data[right])
            left //= 2
            right //= 2

        return minimum
