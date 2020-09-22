'''
You are given an input string.

For each symbol in the string if it's the first character occurrence, replace it with a '1', else replace it with the amount of times you've already seen it...

But will your code be performant enough?
Examples:

input   =  "Hello, World!"
result  =  "1112111121311"

input   =  "aaaaaaaaaaaa"
result  =  "123456789101112"

There might be some non-ascii characters in the string.
'''


def numericals(s):
    base, r = {}, []
    for x in s:
        base[x] = base.get(x, 0) + 1
        r.append(base[x])
    return ''.join(map(str, r))
