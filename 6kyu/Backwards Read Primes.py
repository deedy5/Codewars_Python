'''
Backwards Read Primes are primes that when read backwards in base 10 (from right to left) are a different prime. (This rules out primes which are palindromes.)

Examples:
13 17 31 37 71 73 are Backwards Read Primes

13 is such because it's prime and read from right to left writes 31 which is prime too. Same for the others.
Task

Find all Backwards Read Primes between two positive given numbers (both inclusive), the second one always being greater than or equal to the first one. The resulting array or the resulting string will be ordered following the natural order of the prime numbers.
Example

backwardsPrime(2, 100) => [13, 17, 31, 37, 71, 73, 79, 97] backwardsPrime(9900, 10000) => [9923, 9931, 9941, 9967] backwardsPrime(501, 599) => []
Note for Forth

Return only the first backwards-read prime between start and end or 0 if you don't find any

backwards_prime(2, 100) => [13, 17, 31, 37, 71, 73, 79, 97] 
backwards_prime(9900, 10000) => [9923, 9931, 9941, 9967]
'''


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    sqrtn = int(n**0.5) + 1
    for i in range(5, sqrtn, 6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True
    
def backwards_prime(start, stop): 
    return [x for x in range(start,stop+1) if is_prime(x) and is_prime(int(str(x)[::-1])) and x!=int(str(x)[::-1])]
