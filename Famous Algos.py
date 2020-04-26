# Boyer Moore Majority Vote ALGORITHM

# In the first pass, we generate a single candidate value which is the majority value if there is a majority.
# The second pass simply counts the frequency of that value to confirm. The first pass is the interesting part.
#
# In the first pass, we need 2 values:
# A candidate value, initially set to any value.
# A count, initially set to 0.
#
# For each element in our input list, we first examine the count value. If the count is equal to 0, we set the
# candidate to the value at the current element. Next, first compare the element's value to the current candidate value.
# If they are the same, we increment count by 1. If they are different, we decrement count by 1.

def majority(input):
    candidate = 0
    count = 0
    for value in input:
      if count == 0:
        candidate = value
      if candidate == value:
        count += 1
      else:
        count -= 1
    return candidate if input.count(candidate)>len(input)//2 else None

# Leetcode Majority ELement 2
