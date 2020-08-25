'''
Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
Examples

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Constraints

0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
'''

def valid_parentheses(string):
    base = {')': '('}
    cache = []
    for char in string:
        if cache and base.get(char) == cache[-1]:
            cache.pop()
        elif char in ['(', ')']:
            cache.append(char)
    return cache == []
