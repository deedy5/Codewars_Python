'''
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
Examples

to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
'''

def to_camel_case(text):
    t = text.replace('-', '_').split('_')
    if text.istitle():
        return ''.join(x.title() for x in t)
    return f"{t[0]}{''.join(x.title() for x in t[1:])}"
    
    
