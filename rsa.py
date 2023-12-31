#!/usr/bin/python3
import sys
from random import randrange

c = 1


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


def g(x, c):
    return (x * x + c)


def getf(n):
    global c
    if (n == 1):
        return n
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    if n % 5 == 0:
        return 5
    x = y = 2
    c += 1
    # print(f"c = {c}")
    d = 1

    while d == 1:
        x = g(x, c) % n
        y = g(g(y, c), c) % n
        y = g(g(y, c), c) % n
        d = gcd(abs(x - y), n)
    if d == n or  is_prime(d)== False or is_prime(n // d)== False:
        return getf(n)
    else:
        return d


def is_prime_smaller(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def is_prime(n, prec=5):
    if n < 100:
        return is_prime_smaller(n)
    else:
        for i in range(prec):
            a = randrange(2, n - 2 + 1)
            if pow(a, n - 1, n) != 1:
                return False
    return True


def getFactor(n):
    global c
    c = 1
    isp = is_prime(n)
    if isp:
        return [n, 1]
    p = getf(n)
    return [p, (n // p)]


f = open(sys.argv[1], "r")

for line in f:
    n = int(line)
    p = 1
    if is_prime(n):
        p = 10
        continue
    else:
        p = getf(n)
    print(f"{n}={n // p}*{(p)}")
f.close()
