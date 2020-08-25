'''

You will be given a string and you task is to check if it is possible to convert that string into a palindrome by removing a single character. If the string is already a palindrome, return "OK". If it is not, and we can convert it to a palindrome by removing one character, then return "remove one", otherwise return "not possible". The order of the characters should not be changed.

For example:

solve("abba") = "OK". -- This is a palindrome
solve("abbaa") = "remove one". -- remove the 'a' at the extreme right. 
solve("abbaab") = "not possible". 

'''

def solve(s):
    if s[::-1] == s:
        return 'OK'
    if s[1::][::-1] == s[1:]:    
        return "remove one"
    if s[:-1][::-1] == s[:-1]:
        return "remove one"
    for i in range(len(s)):
        t = f'{s[:i]}{s[i+1:]}'
        if t == t[::-1]:
            return "remove one"        
    return "not possible"
