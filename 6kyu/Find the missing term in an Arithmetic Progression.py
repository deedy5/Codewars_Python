'''
An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a given series of numbers. You are provided with consecutive elements of an Arithmetic Progression. There is however one hitch: exactly one term from the original series is missing from the set of numbers which have been given to you. The rest of the given series is the same as the original AP. Find the missing term.

You have to write a function that receives a list, list size will always be at least 3 numbers. The missing term will never be the first or last one.
Example

find_missing([1, 3, 5, 9, 11]) == 7

PS: This is a sample question of the facebook engineer challenge on interviewstreet. I found it quite fun to solve on paper using math, derive the algo that way. Have fun!
'''


'''
#v1 -- bad---

from collections import Counter
def find_missing(sequence):
    t = Counter(sequence[i]-sequence[i-1] for i in range(1, len(sequence))).most_common()
    for i in range(1, len(sequence)):
        if sequence[i] - sequence[i-1] == t[1][0]:
            return sequence[i] - t[0][0]
'''

#v2
def find_missing(sequence):
    interval = (sequence[-1] - sequence[0]) / len(sequence)
    for i,v in enumerate(sequence):
        if sequence[i+1] - v != interval:
            return v + interval
