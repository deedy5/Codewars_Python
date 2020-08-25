'''

Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

Your task is to process a string with "#" symbols.
Examples

"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""

'''

def clean_string(s):
    r = []
    for char in s:
        if r and char == '#':
            r.pop()
        elif char != '#':
            r.append(char)
    return ''.join(r)
