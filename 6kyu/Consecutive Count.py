'''
I want to know the size of the longest consecutive elements of X in Y. You will receive two arguments: items and key. Return the length of the longest segment of consecutive keys in the given items.

Notes:

    The items and the key will be either an integer or a string (consisting of letters only)
    If the key does not appear in the items, return 0

Examples

90000, 0           -->  4
"abcdaaadse", "a"  -->  3
"abcdaaadse", "z"  -->  0
'''


from itertools import groupby
def get_consective_items(items, key):
    items, key = str(items), str(key)
    return max((len(list(v)) for x,v in groupby(items) if x==key), default=0)
