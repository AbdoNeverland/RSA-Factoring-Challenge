
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

print(getf(239809320265259))