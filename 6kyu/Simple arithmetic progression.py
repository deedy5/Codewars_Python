'''
In this Kata, you will be given an array of integers and your task is to return the number of arithmetic progressions of size 3 that are possible from that list. In each progression, the differences between the elements must be the same.

[1, 2, 3, 5, 7, 9] ==> 5
// [1, 2, 3], [1, 3, 5], [1, 5, 9], [3, 5, 7], and [5, 7, 9]

All array elements will be unique and sorted.
'''


from itertools import combinations

def solve(arr):
    r = 0
    for x in combinations(arr, 3):
        if sum(x) / len(x) == x[1]:
            r += 1
    return r
