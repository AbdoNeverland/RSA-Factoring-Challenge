import math
c = 1
def gcd(x,y):
    if y == 0:
        return x
    return gcd(y, x % y)
def g(x, c):
    return (x*x +c)

def getf(n):
    global c
    if (n == 1):
        return n    
    x = y = 2
    c +=1
    d=1

    while d ==1:
        x=g(x,c) % n
        y=g(g(y, c),c) %n
        y=g(g(y, c),c) %n
        d=gcd(abs(x - y), n)

    if d == n: 
        return getf(n)
    else:
        return d
def isPrime(n):
    for i in range(2, int(math.sqrt(n))):
        if n%i == 0:
            return i
    return -1
print(isPrime(719310057817))
#print(getf(193993833211))