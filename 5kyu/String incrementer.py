'''
Your job is to write a function which increments a string, to create a new string.

    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
'''

'''
# v1
def increment_string(strng):
    print(strng)
    nlist = []
    for i in range(len(strng)-1, -1, -1):
        if strng[i].isdigit():
            nlist.append(strng[i])
        else: break
    ns = ''.join(reversed(nlist))
    ss = f"{strng[:len(strng)-len(ns)]}"
    if not nlist:
        return f"{ss}1"
    num = f"{int(ns)+1:0{len(ns)}}"
    return f"{ss}{num}"
'''

# v2
def increment_string(strng):
    ss = strng.rstrip('0123456789')
    ns = strng[len(ss):]
    if ns == '':
        return f"{ss}1"
    return f"{ss}{int(ns)+1:0{len(ns)}}"
