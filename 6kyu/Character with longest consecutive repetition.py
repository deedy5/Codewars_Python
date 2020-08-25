'''
Description:

For a given string s find the character c (or C) with longest consecutive repetition and return:

(c, l)

where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.

For empty string return:

('', 0)
'''

from itertools import groupby
def longest_repetition(chars):
    if chars == "":
        return ('', 0)
    t = [(k, sum(1 for y in x)) for k,x in groupby(chars)]
    r = max(t, key = lambda x: x[1])
    return r
