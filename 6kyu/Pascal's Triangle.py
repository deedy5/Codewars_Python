'''
Pascal's Triangle

Wikipedia article on Pascal's Triangle: http://en.wikipedia.org/wiki/Pascal's_triangle

Write a function that, given a depth (n), returns a single-dimensional array/list representing Pascal's Triangle from the first to the n-th level.

For example: pascals_triangle(4) == [1, 1, 1, 1, 2, 1, 1, 3, 3, 1]
'''

def pascals_triangle(n):
    res, r = [], []
    for x in range(n):        
        l = len(r)
        r = [1 if i == 0 or i == l else r[i-1]+r[i] for i in range(l+1)]
        res.extend(r)
    return res
    
