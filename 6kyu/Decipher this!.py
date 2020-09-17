'''
You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

For each word:

    the second and the last letter is switched (e.g. Hello becomes Holle)
    the first letter is replaced by its character code (e.g. H becomes 72)

Note: there are no special characters used, only letters and spaces

Examples

decipherThis('72olle 103doo 100ya'); // 'Hello good day'
decipherThis('82yade 115te 103o'); // 'Ready set go'
'''


def decipher_this(string):
    slist = string.split()
    r = []
    for word in slist:
        nums = [x for x in word if x.isdigit()] 
        chars = [x for x in word if x.isalpha()]
        w0 = chr(int(''.join(nums)))        
        if len(chars) > 1:
            chars[0], chars[-1] = chars[-1], chars[0]
        w = ''.join(chars)
        r.append(f"{w0}{w}")
    return ' '.join(r)
