# Using Recursion finding the longest palindromic substring in a string

def checkPalindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False

sub = '' 
d = {}                       # for memoization

def getMax(s):
    global sub
    global d

    d[s] = 1
    if checkPalindrome(s):
        if len(s)>len(sub):
            sub = s
    else:
        a = s[1:]
        if a not in d:
            getMax(a)

        b = s[:-1]
        if b not in d:
            getMax(b)

getMax('geeksnitingeeks')
print(sub)




