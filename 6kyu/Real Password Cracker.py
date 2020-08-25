'''

You are a h4ck3r n00b: you "acquired" a bunch of password hashes, and you want to decypher them. Based on the length, you already guessed that they must be SHA-1 hashes. You also know that these are weak passwords: maximum 5 characters long and use only lowercase letters (a-z), no other characters.

Happy hacking!

Notes:

    pre-generating the full hash table is not advised, due to the time-limit on the CW platform
    there will be only a few tests for 5-letter words (hint: start from the beginnig of the alphabet)

'''

import hashlib
from string import ascii_lowercase
from itertools import product

def password_cracker(hash):
    for repeat in range(6):
        for m in product(ascii_lowercase, repeat=repeat):
            t = ''.join(m).encode()
            r = hashlib.sha1(t).hexdigest()
            if hash == r:
                return t.decode()
