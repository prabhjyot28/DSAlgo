
# we want to substring in a string.

# Naive ALGORITHM  , Time O(mn)

# Knuth Morris Prat Algorithm
# The idea is to find the longest suffix that is also the prefix and start searching the pattern again from this point.

pat = 'ABABCABAB'
lps = [0]*len(pat)    # lps[i] represents longest suffix which is also prefix of pattern[:i+1]


j = 0
i = 1

while i<len(pat):

    if pat[i]==pat[j]:
        j+=1
        lps[i] = j
        i+=1
    else:
        if j!=0:
            j = lps[j-1]
        else:
            lps[i]=0
            i+=1


# Rabin Karp Algorithm,   Avergae time - O(n+m), Worst Case - O(n^2)
# use a rolling hash function to compare values.
pattern = 'abc'
def hash(patten):
    val = 0
    for i in range(len(pattern)):
        val += (ord(pattern[i]) * (26**(len(pattern)-i-1)))
    return val%(10**9+7)
    
