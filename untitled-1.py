import random
from random import randrange

def is_large_prime(n, k=5): # miller-rabin
    from random import randint
    if n < 2: return False
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n % p == 0: return n == p
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d>>1
    for i in range(k):
        x = pow(randint(2, n-1), (d), n)
        if x == 1 or x == n-1: continue
        for r in range(1, s):
            x = (x * x) % n
            if x == 1: return False
            if x == n-1: break
        else: return False
    return True
# Iterative Function to calculate
# (a^n)%p in O(logy)
def power(a, n, p):

    # Initialize result
    res = 1

    # Update 'a' if 'a' >= p
    a = a % p 

    while n > 0:

        # If n is odd, multiply
        # 'a' with result
        if n % 2:
            res = (res * a) % p
            n = n - 1
        else:
            a = (a ** 2) % p

            # n must be even now
            n = n // 2

    return res % p

# If n is prime, then always returns true,
# If n is composite than returns false with
# high probability Higher value of k increases
# probability of correct result
def is_prime_smaller(n):
    for i in range(2, n // 2):
        if n%i == 0:
            return False
    return True
def is_prime(n, prec=3):
    if n < 100:
        return is_prime_smaller(n)
    else:
        a = randrange(2, n - 2+1)
        if pow(a, n - 1, n) != 1:
            return False
    return True
print(is_prime(37))
#print(getf(193993833211))