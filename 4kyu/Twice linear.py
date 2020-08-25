'''
Consider a sequence u where u is defined as follows:

    The number u(0) = 1 is the first one in u.
    For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
    There are no other numbers in u.

Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...
Task:

Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).
Example:

dbl_linear(10) should return 22
Note:

Focus attention on efficiency
'''

import bisect
def dbl_linear(n):
    u, i, cache, t2 = [1,], 0, set(), 0
    while len(u) < n * 2:
        t1 = u[i] * 2 + 1
        t2 = u[i] * 3 + 1
        if t1 not in cache:
          if t1 > u[-1]:
              u.append(t1)
          else:
              bisect.insort(u, t1)
          cache.add(t1)
        if t2 not in cache:
          if t2 > u[-1]:
              u.append(t2)
          else:
              bisect.insort(u, t2)
          cache.add(t2)
        i += 1
    return u[n]
