'''
For building the encrypted string:
Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
Do this n times!

Examples:

"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"

Write two methods:

def encrypt(text, n)
def decrypt(encrypted_text, n)

For both methods:
If the input-string is null or empty return exactly this value!
If n is <= 0 then return the input text.

This kata is part of the Simple Encryption Series:
Simple Encryption #1 - Alternating Split
Simple Encryption #2 - Index-Difference
Simple Encryption #3 - Turn The Bits Around
Simple Encryption #4 - Qwerty
'''

def decrypt(etext, n):
    if n <= 0:
        return etext
    s = len(etext)//2
    for _ in range(n):        
        a, b = etext[:s], etext[s:]
        etext = ''.join(f'{b[i:i+1]}{a[i:i+1]}' for i in range(s+1))
    return etext

def encrypt(text, n):
    for _ in range(n):
        text = f"{text[1::2]}{text[::2]}"
    return text
