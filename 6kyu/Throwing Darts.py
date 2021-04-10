'''
You've just recently been hired to calculate scores for a Dart Board game!

Scoring specifications:

    0 points - radius above 10
    5 points - radius between 5 and 10 inclusive
    10 points - radius less than 5

If all radii are less than 5, award 100 BONUS POINTS!

Write a function that accepts an array of radii (can be integers and/or floats), and returns a total score using the above specification.

An empty array should return 0.
Examples:

scoreThrows( [1, 5, 11] )    =>  15
scoreThrows( [15, 20, 30] )  =>  0
scoreThrows( [1, 2, 3, 4] )  =>  140
'''

def score_throws(radii):
    if not radii:
        return 0
    f = 0
    summ = 0
    for p in radii:
        if p < 5:
            summ += 10
        elif 5 <= p <= 10:
            summ += 5
            f = 1
        elif p > 10:
            f = 1
    if f == 0:
        summ += 100
    return summ
    
