'''
Your job is to change the string s using a non-negative integer n.

Each bit in n will specify whether or not to swap the case for each alphabetic character in s. When you get to the last bit of n, circle back to the first bit. If the bit is 1, swap the case. If its 0, don't swap the case.

You should skip the checking of bit when a non-alphabetic character is encountered, but they should be preserved in their original positions.

For example,

swap('Hello world!', 11) == 'heLLO wORLd!'
# because bin(11) is 1011 so the first, third, fourth, fifth, seventh, eighth, and ninth alphabetical characters have cases swapped
'H e l l o  w o r l d !'
'1 0 1 1 1  0 1 1 1 0'
'^   ^ ^ ^    ^ ^ ^   '

swap('', 11345) == ''
swap('the lord of the rings', 0) == 'the lord of the rings'
'''

from itertools import cycle
def swap(s,n):
    codegen = (x for x in cycle(f"{n:0b}"))
    r = []
    for char in s:
        if char.isalpha():
            if next(codegen) == '1':
                char = char.swapcase()
        r.append(char)
    return ''.join(r)
