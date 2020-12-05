'''
Given an integer n return "odd" if the number of its divisors is odd. Otherwise return "even".

Note: big inputs will be tested.
Examples:

All prime numbers have exactly two divisors (hence "even").

For n = 12 the divisors are [1, 2, 3, 4, 6, 12] – "even".

For n = 4 the divisors are [1, 2, 4] – "odd".
'''


def oddity(n):
    if n**0.5 % 1 == 0:
        return "odd" 
    return "even"
