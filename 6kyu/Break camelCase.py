'''
Complete the solution so that the function will break up camel casing, using a space between words.
Example

solution("camelCasing")  ==  "camel Casing"
'''

def solution(s):
    return ''.join(f" {x}" if x.isupper() else x for x in s)
