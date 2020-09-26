'''
In this Kata, you will be given a number and your task will be to return the nearest prime number.

solve(4) = 3. The nearest primes are 3 and 5. If difference is equal, pick the lower one. 
solve(125) = 127

We'll be testing for numbers up to 1E10. 500 tests.
'''


def solve(n): 
    
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        sqrtn: int = int(n**0.5) + 1
        for i in range(5, sqrtn, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    if is_prime(n):
            return n
    step = (n % 2) + 1
    while True:
        if is_prime(n - step):
            return n - step
        if is_prime(n + step):
            return n + step
        step += 2
