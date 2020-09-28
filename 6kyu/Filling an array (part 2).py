'''
Following on from Part 1, part 2 looks at some more complicated array contents.

So let's try filling an array with...
...square numbers

The numbers from 1 to n*n

const squares = n => ???
squares(5) // [1, 4, 9, 16, 25]

...a range of numbers

A range of numbers starting from start and increasing by step

const range = (n, start, step) => ???
range(6, 3, 2) // [3, 5, 7, 9, 11, 13]

...random numbers

A bunch of random integers between min and max

const random = (n, min, max) => ???
random(4, 5, 10) // [5, 9, 10, 7]

...prime numbers

All primes starting from 2 (obviously)...

const primes = n => ???
primes(6) // [2, 3, 5, 7, 11, 13]

HOTE: All the above functions should take as their first parameter a number that determines the length of the returned array.
'''


from random import randint

def squares(n):
    return [x*x for x in range(1, n+1)]

def num_range(n, start, step):
    end = start + n * step
    return [x for x in range(start, end, step)]

def rand_range(n, mn, mx):
    return [randint(mn, mx) for _ in range(n)]

def sieve6g(limit):
        #sieve of Eratosthenes generator    
        a = [True] * limit
        a[0] = a[1] = False
        for (i, isprime) in enumerate(a):
            if isprime:
                yield i
                for n in range(i*i, limit, i):
                    a[n] = False
                    
def primes(n):
    r = []
    for x in sieve6g(1000000):
        r.append(x)
        if len(r) == n:
            return r

