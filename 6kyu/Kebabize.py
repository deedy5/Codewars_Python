'''
Modify the kebabize function so that it converts a camel case string into a kebab case.

kebabize('camelsHaveThreeHumps') // camels-have-three-humps
kebabize('camelsHave3Humps') // camels-have-humps

Notes:

    the returned string should only contain lowercase letters
'''


def kebabize(string):
    return (''.join(f"-{x.lower()}" if x.isupper() else x for x in string if x.isalpha())).lstrip('-')
