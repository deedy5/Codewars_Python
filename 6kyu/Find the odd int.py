'''
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
'''

from collections import Counter
def find_it(seq):
    t = Counter(seq)
    for i in t:
        if t[i] % 2 != 0:
            return i
        
