'''
Your task, is to create NxN multiplication table, of size provided in parameter.

for example, when given size is 3:

1 2 3
2 4 6
3 6 9

for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]
'''

# v1
def multiplication_table(size):
    r = []
    for x in range(1, size+1):
        t = []
        for y in range(1, size+1):
            t.append(y*x)
        r.append(t)
    return r
