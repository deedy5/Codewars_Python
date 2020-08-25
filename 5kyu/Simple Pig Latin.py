'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''

def pig_it(text):
    t = text.split()
    return ' '.join(f"{x[1:]}{x[:1]}ay" if x not in ['!','?'] else x for x in t)
