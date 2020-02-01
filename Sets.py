

# # sets does not maintains any order (no indexing), hence no slicing too.

# # sets are mutable (changable)
# s = {1,2,3}

# print(type(s))
# print(s)

# l = ['a', 'b', 'c']

# s1 = set(l)

# print(s1)


# # Frozenset are immutable

# fs = frozenset([4,5,6])

# print(type(fs))
# print(fs)


# # Basic operations on sets

# s.add(4)
# s.add(5)


# print(5 in s)       # look up 

# print(s)

# print(s.union(s1))   # s|s1

# print(s.intersection(s1))   # s&s1

# print(s.difference(s1))    #  s-s1

# print(s.clear())     # Removes all elements (clears) from the set


# print(s==s1)    # checks equivalent
# print(s<=s1)    # s is subset of s1
# print(s<s1)     # s is proper subset of s1
# print(s1>=s2)    # s1 is superset of s2
# print(s1>s2)     # s1 is proper superset of s2


# # Discard and remove both deletes element but if element is not present remove
# # method gives error.

# s.discard(element)
# s.remove(element)


# Disjoint Sets

# s1 = {1,2,3}
# s2 = {4,5,6}

# print(s1.isdisjoint(s2))    # True  

# iddisjoint() check whether both sets have any node in common or not.






# # Built in function with sets

# len(s)
# max(s)
# min(s)
# sorted(s)
# sum(s)

#----------------------------------------#


# Sets can only contains hashable items not like list beacuse lists 
# are mutable (not hashable).

# s = set([['a', 'b'], ['c', 'd']])            
# print(s)           


# Sets are Mutable but cant contain mutable (non hashable) items.


#------------------------------------------#

# Average time complexity for lookup/ insertion/ deletion in set is O(1).







