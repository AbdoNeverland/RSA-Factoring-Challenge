#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int c = 1;


long long int  gcd(long long int x, long long int y)
{
    if (y == 0)
        return (x);
    return gcd(y, x % y);
}

long long int g(long long int x, long long int c)
{
    return (x * x + c);
}


long long int getf(long long int n)
{
    int k;
    long long int x, y,d;
    if (n == 1)
        return n;
    for (k = 2; k < 10; k++)
    {
        if (n % k == 0)
            return k;
    }
    x = y = 2;
    c += 1;
    d = 1;

    while (d == 1)
    {
        x = g(x, c) % n;
        y = g(g(y, c), c) % n;
        y = g(g(y, c), c) % n;
        d = gcd(abs(x - y), n);
    }

    if (d == n)
        return getf(n);
    else
        return d;
}

int is_prime_smaller(long long int n)
{
    long long int i;
    for (i = 2; i < n; i++)
    {
        if (n % i == 0)
            return 0;
    }
    return 1;
}
 int powmod(int base, int e, int m)
 {
    long long int x=1, y=base; 
    while (e > 0) {
        if (e % 2 == 1)
            x = (x*y) % m;
        y = (y*y) % m;
        e /= 2;
    }
    return x % m;
}
int is_prime(long long int n)
{
    int i;
    long long int a;
    int prec=1;

    if (n < 10)
        return is_prime_smaller(n);
    else
    {
        for( i =0; i< prec; i++)
        {
            a =  (rand() % (n+1));
            if (powmod(a, n - 1, n) != 1)
                return 0;
        }
    }
    return 1;
}


int main(int argc, char ** argv)
{
    FILE *f;
    char *line = NULL;
	size_t length = 0;
    ssize_t readed;
    long long int number, p, q;
printf("is %d prime : %d", 7,is_prime(1718944270642558716715));

if (argc != 2)
    exit(1);
    f = fopen(argv[1], "r");
	if (f == NULL) 
		exit(1);

        while ((readed = getline(&line, &length, f)) != -1)
        {
            number = atoll(line);
            p = 1;
            if (is_prime(number))
            p = 1;
            else
            p = getf(number);
            q = number / p;
            printf("%lld=%lld*%lld\n", number, p , q);
	}
    free(line);
    fclose(f);

}