

from sortedcontainers import SortedList
sl = SortedList([1,2,3,4,0,-1,2], key = lambda x: -x)         # O(nlogn)

sl.add(val)    # O(logn)
sl.update(iterable)   # O(klogn)   (iterable of size k)


sl.clear()      # O(n)  (Removes all values from sl)
sl.discard(val)     #O(logn)  [Error free]
sl.remove(val)      #O(logn)   [Gives error]
sl.pop(index)      #O(logn)

sl.index(val, start=None, stop=None)
sl.bisect_left(val)   # O(logn)
sl.bisect_right(val)   #O(logn)


sl.count(val)    # O(logn)
sl.copy()    # O(n)  returns a shallow copy

# reversed()  and len() and for-in and in operator





-------------------------------------------------------------------------------------------------

from sortedcontainers import SortedSet
ss = SortedSet()   # everything same as SortedList but no duplicates
ss.difference(iterable)   # return new sorted set   (ss-itertable)
ss.difference_update(iterable)   # updates itself.
ss.intersection(iterable)   # ss & iterable
ss.intersection_update(iterable)
ss.symmetric_difference(iterable)   # ss ^ iterable  # values which are exactly in one.
ss.symmetric_difference_update(iterable)
ss.union(iterable)    # ss |= iterable    (update itself)


---------------------------------------------------------------------------------------------------





from sortedcontainers import SortedDict
sd  = SortedDict()    # keys are maintained in sorted order.

# adding a key takes O(logn) time.
sd['b'] = 1
sd['a'] = 2
sd['c'] = 3

d = {'c':3, 'a':2, 'b':1}
print(sd==d)   # True


del sd['b']   # O(logn) time
sd.clear()   # O(n)
sd.pop(key)    # O(logn)
sd.popitem(ind)    # return (key, val) pair from ind O(logn)
sd.peekitem(ind)  # return (key, val) pair at ind    O(logn)

sd.keys()
sd.items()
sd.values()
sd.bisect_left(key)
sd.bisect_right(key)
sd.index()
