'''
In this Kata, you will be given an array of strings and your task is to remove all consecutive duplicate letters from each string in the array.

For example:

    dup(["abracadabra","allottee","assessee"]) = ["abracadabra","alote","asese"].

    dup(["kelless","keenness"]) = ["keles","kenes"].

Strings will be lowercase only, no spaces.
'''


from itertools import groupby
def dup(arry):
    return [''.join(x[0] for x in groupby(word)) for word in arry]
