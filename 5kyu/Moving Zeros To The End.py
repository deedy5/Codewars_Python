'''
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]
'''

def move_zeros(array):
    t = [x for x in array if x!=0 or x is False]
    t0 = (len(array) - len(t))
    t1 = [0 for x in range(t0)]
    return [*t, *t1]
