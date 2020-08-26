'''
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.
Examples:

tickets([25, 25, 50]) # => YES 
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
'''

from collections import Counter
def tickets(people):
    cache = []
    for x in people:
        if x == 25:
            cache.append(x)
        if x == 50:
            try:
                cache.remove(25)
                cache.append(50)
            except:
                return "NO"
        if x == 100:
            t = Counter(cache)
            if t[50] >= 1 and t[25] >= 1:
                cache.remove(50)
                cache.remove(25)
                cache.append(x)
            elif t[25] >= 3:
                cache.remove(25)
                cache.remove(25)
                cache.remove(25)
                cache.append(x)
            else:
                return "NO"
    return "YES"
                
        
