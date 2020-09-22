'''
Reverse every other word in a given string, then return the string. 
Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word. 
Punctuation marks should be treated as if they are a part of the word in this kata.
'''


def reverse_alternate(string):
    s = string.split()
    return ' '.join(x[::-1] if i%2==0 else x for i,x in enumerate(s,1))
