'''
Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

    the array can't be empty
    only non-negative, single digit integers are allowed

Return nil (or your language's equivalent) for invalid inputs.
Examples

For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6]
'''


def up_array(arr):
    if arr == []:
        return None
    num = []
    for c in arr:
        if c < 0 or c > 9:
            return None
        num.append(c)
    num = int(''.join(f"{x}" for x in num)) + 1
    r = []
    for n in f"{num}":        
        if len(n) > 1:
            return None
        r.append(n)
    return [int(x) for x in r]
