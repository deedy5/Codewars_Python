'''
Take an input string and return a string that is made up of the number of occurences of each english letter in the input followed by that letter, sorted alphabetically. The output string shouldn't contain chars missing from input (chars with 0 occurence); leave them out.

An empty string, or one with no letters, should return an empty string.

Notes:

    the input will always be valid;
    treat letters as case-insensitive

Examples

"This is a test sentence."  ==>  "1a1c4e1h2i2n4s4t"
""                          ==>  ""
"555"                       ==>  ""
'''


from collections import Counter
def string_letter_count(s):
    s = s.lower()
    slist = [x for x in s if x.isalpha()]
    t = sorted(Counter(slist).items())
    return ''.join(f"{x[1]}{x[0]}" for x in t)
