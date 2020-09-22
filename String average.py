'''
You are given a string of numbers between 0-9. Find the average of these numbers and return it as a floored whole number (ie: no decimal places) written out as a string. Eg:

"zero nine five two" -> "four"

If the string is empty or includes a number greater than 9, return "n/a"
'''


def average_string(s):
    base = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
            'five': 5, 'six': 6,'seven': 7, 'eight': 8, 'nine': 9}
    basen = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 
            5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    try:
        return basen[int(sum(base[x] for x in s.split()) / len(s.split()))]
    except:
        return 'n/a'
    
