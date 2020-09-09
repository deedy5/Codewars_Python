'''
Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

    i increments the value (initially 0)
    d decrements the value
    s squares the value
    o outputs the value into the return array

Invalid characters should be ignored.

parse("iiisdoso")  ==>  [8, 64]
'''

def parse(data):
    r = []
    t = 0
    for x in data:
        if x == 'i':
            t += 1
        elif x == 'd':
            t -= 1
        elif x == 's':
            t *= t
        elif x == 'o':
            r.append(t)
    return r
