'''
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''

Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.
'''

def namelist(names):
    t = [x['name'] for x in names]
    if len(t) >= 3:
        return f"{', '.join(t[:-2])}, {t[-2]} & {t[-1]}"
    if len(t) == 2:
        return f"{t[0]} & {t[1]}"
    if len(t) == 1:
        return f"{t[0]}"
    if len(t) == 0:
        return ''
