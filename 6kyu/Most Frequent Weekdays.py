'''
What is your favourite day of the week? Check if it's the most frequent day of the week in the year.

You are given a year as integer (e. g. 2001). You should return the most frequent day(s) of the week in that year. The result has to be a list of days sorted by the order of days in week (e. g. ['Monday', 'Tuesday'], ['Saturday', 'Sunday'], ['Monday', 'Sunday']). Week starts with Monday.

Input: Year as an int.

Output: The list of most frequent days sorted by the order of days in week (from Monday to Sunday).

Preconditions:

    Week starts on Monday.
    Year is between 1583 and 4000.
    Calendar is Gregorian.

Example:

most_frequent_days(2427) == ['Friday']
most_frequent_days(2185) == ['Saturday']
most_frequent_days(2860) == ['Thursday', 'Friday']
'''


#Solution is stupid

from datetime import timedelta, date
from collections import Counter
import calendar

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def most_frequent_days(year):      
    start_date = date(year, 1, 1)
    end_date = date(year, 12, 31)
    t = Counter(x.weekday() for x in daterange(start_date, end_date)).most_common(2)
    base = list(calendar.day_name)
    if t[0][1] == t[1][1]:
        return [base[t[0][0]]]
    if t[0][0] == 6 and t[1][0] == 0:
        return ['Monday', 'Sunday']
    return [base[t[0][0]], base[t[1][0]]]
