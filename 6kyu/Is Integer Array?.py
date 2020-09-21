'''
Write a function with the signature shown below:

def is_int_array(arr):
    return True

    returns true / True if every element in an array is an integer or a float with no decimals.
    returns true / True if array is empty.
    returns false / False for every other input.
'''


def is_int_array(arr):
    if arr == None or arr == '':
        return False    
    for x in arr:
        try:
            if x//1 != x:
                return False
        except:
            return False
    return True
