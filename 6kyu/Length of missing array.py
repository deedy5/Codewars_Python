'''
You get an array of arrays.
If you sort the arrays by their length, you will see, that their length-values are consecutive.
But one array is missing!


You have to write a method, that return the length of the missing array.

Example:
[[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]] --> 3


If the array of arrays is null/nil or empty, the method should return 0.

When an array in the array is null or empty, the method should return 0 too!
There will always be a missing element and its length will be always between the given arrays. 
'''


def get_length_of_missing_array(array_of_arrays):
    setlen = set()
    for array in array_of_arrays:
        if not array or array == []:
            return 0
        setlen.add(len(array))
    if not setlen:
        return 0
    mina, maxa = min(setlen), max(setlen)+1
    for i in range(mina, maxa):
        if i not in setlen:
            return i
