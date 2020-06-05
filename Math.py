import math

math.gcd(a, b)      # GCD/ HCF of a and b
math.factorial(x)    #x!
math.comb(n, k)      # nCk
# Number of ways to choose k items from n, without repetition and with out order

math.perm(n, k)      # nPk
#Number of ways to choose k items from n, without repetitions and with order.

 math.log(num, base = e)
 math.log2(num)
 math.log10(num)

# If a number n is not a prime, it can be factored into two factors a and b:
# n = a * b
# If both a and b were greater than the square root of n, then a * b would be greater than n.
# So at least one of those factors must be less than or equal to the square root of n,
# and if we can't find any factors less than or equal to the square root, n must be prime.


 #---------------------------------------------Binary Exponentiation-------------------------#
# O(logn)  multiplications.

 def pow(a, n):
     if n==0:
         return a

    half = pow(a, n//2)
    if n%2:
        return half*half*a
    else:
        return half*half


# 13 == 1101
# 3^13  = 3^8 . 3^4. 3^1
def pow(a, b):
    ans = 1
    while b:
        if b&1:
            ans = ans*a
        a = a*a
        b = b>>1
    return ans

# Fast Modular Exponentiation
# a^n % M   == (a^(n/2) % M * a^(n/2) % M) % M




# ---------------------------------------------Euclid's Algo--------------------------#
# O(log(min(a, b)))
def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)


# GCD==HCF   and   LCM(a, b) == (a.b)/(GCD(a, b))

#  ax+by = g     # extended euclidean algo.
def gcd(a, b):
    if b==0:
        return a, 1, 0
    else:
        g, x, y = gcd(b, a%b)
        return g, y, x-y*(a//b)




#------------------------------Fibonacci Numbers----------------------#
# 0,1,1,2,3,5,8,13......
Fn = round[((1+root(5))/2)^n / root(5)]

GCD(Fm, Fn) = F(GCD(m, n))


# --------------------------------------Prime Numbers--------------------------------#

All even numbers except 2 are composites.

# PRIMARILTY TEST
def check(num):
    d = 2
    while d*d<=num:
        if num%d==0:
            return False
        d+=1
    return True



#----------------------------------------------Modular Arithmetic-----------------------------#

(a+b)%m = (a%m + b%m)%m
(a-b)%m = (a%m - b%m)%m
(a*b)%m = (a%m * b%m)%m
# Not hold true in case of division.

mod(x, m) = x%m if x%m >=0 else x%m+m




# Pigeonhole principle
# Inclusion - exclusion principle.
# Cyclic Pemutations
# Floyd's Cycle detection Algorithm.




# FORMULAS

Triangle-
validity = a+b>c and b+c>a and c+a>b
area = sqrt(p*(p-a)*(p-b)*(p-c))  where p = half of perimeter.

# POINTS-
- A number is divisible by 9 if and only if sum of its digits is divisible by 9. (Digital Root)
