'''
Finish the solution so that it takes an input n (integer) and returns a string that is the decimal representation of the number grouped by commas after every 3 digits.

Assume: 0 <= n < 2147483647
Examples

       1  ->           "1"
      10  ->          "10"
     100  ->         "100"
    1000  ->       "1,000"
   10000  ->      "10,000"
  100000  ->     "100,000"
 1000000  ->   "1,000,000"
35235235  ->  "35,235,235"
'''

def group_by_commas(n):
    return f'{n:,}'

'''#v2
def group_by_commas(n):
    ns = str(n)
    lns = len(ns)
    return ''.join(f",{x}" if (lns-i)%3==0 and i!=0 else x for i,x in enumerate(ns))
'''
