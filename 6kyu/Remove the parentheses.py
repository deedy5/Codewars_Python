'''
Remove the parentheses

In this kata you are given a string for example:

"example(unwanted thing)example"

Your task is to remove everything inside the parentheses as well as the parentheses themselves.

The example above would return:

"exampleexample"

Notes

    Other than parentheses only letters and spaces can occur in the string. Don't worry about other brackets like "[]" and "{}" as these will never appear.
    There can be multiple parentheses.
    The parentheses can be nested.
'''


def remove_parentheses(s):
    r, cache = [], []
    m = 1
    for c in s:
        if c == '(':
            cache.append('(')
            m = 0
        elif c == ')':
            cache.pop()
            if not cache:
                m = 1
        elif m == 1:
            r.append(c)
    return ''.join(r)
