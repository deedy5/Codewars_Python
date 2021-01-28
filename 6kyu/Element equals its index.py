'''
Given a sorted array of distinct integers, write a function index_equals_value that returns the lowest index for which array[index] == index.
Return -1 if there is no such index.

Your algorithm should be very performant.

[input] array of integers ( with 0-based nonnegative indexing )
[output] integer
Examples:

input: [-8,0,2,5]
output: 2 # since array[2] == 2

input: [-1,0,3,6]
output: -1 # since no index in array satisfies array[index] == index
'''


def index_equals_value(arr):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = lo + hi >> 1
        if arr[mid] >= mid:
            hi = mid
        else:
            lo = mid + 1
    return lo if lo < len(arr) and arr[lo] == lo else -1
