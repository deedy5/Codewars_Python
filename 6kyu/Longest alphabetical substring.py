'''
Find the longest substring in alphabetical order.

Example: the longest alphabetical substring in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".

There are tests with strings up to 10 000 characters long so your code will need to be efficient.

The input will only consist of lowercase characters and will be at least one letter long.

If there are multiple solutions, return the one that appears first.
'''


def longest(s):
    r = []
    for i,x in enumerate(s):
        temp = [x]
        for j in range(i+1, len(s)):
            if s[j] >= temp[-1]:
                temp.append(s[j])
            else:
                r.append(''.join(temp))
                break
        r.append(''.join(temp))
    return max(r, key=len)
