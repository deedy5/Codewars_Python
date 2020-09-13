'''
Longest Palindrome

Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, the return value must be 0.
Example:

"a" -> 1 
"aab" -> 2  
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0
'''


def longest_palindrome (s):
    maxlen, lens = 0, len(s)
    for i in range(lens):
        for j in range(lens, i, -1):
            if j - i < maxlen:
                break
            t = s[i:j+1]
            if t == t[::-1]:
                maxlen = max(len(t), maxlen)
                break
    return maxlen
