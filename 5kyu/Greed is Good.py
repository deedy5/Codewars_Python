'''
Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point

A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)

In some languages, it is possible to mutate the input to the function. This is something that you should never do. If you mutate the input, you will not be able to pass all the tests.
'''

# v1
from collections import Counter
def score(dice):
    base = {1: {1: 100, 3: 1000}, 2: {3: 200}, 3: {3: 300},
            4: {3: 400}, 5: {1: 50, 3: 500}, 6: {3: 600},}
    dc = Counter(dice)
    r = 0
    for x in dc:
        print(x, dc[x])
        if dc[x] == 4:
            r += base.get(x, 0).get(3, 0) + base.get(x, 0).get(1, 0)
        if dc[x] == 5:
            r += base.get(x, 0).get(3, 0) + base.get(x, 0).get(1, 0) + base.get(x, 0).get(1, 0)
        if dc[x] == 6:
            r += base.get(x, 0).get(6, 0) * 2
        if dc[x] == 2:
            r += base.get(x, 0).get(1, 0) * 2
        else:
            r += base.get(x, 0).get(dc[x], 0)
    return r
