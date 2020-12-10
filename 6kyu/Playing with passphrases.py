'''
Everyone knows passphrases. One can choose passphrases from poems, songs, movies names and so on but frequently they can be guessed due to common cultural references. You can get your passphrases stronger by different means. One is the following:

choose a text in capital letters including or not digits and non alphabetic characters,

    shift each letter by a given number but the transformed letter must be a letter (circular shift),
    replace each digit by its complement to 9,
    keep such as non alphabetic and non digit characters,
    downcase each letter in odd position, upcase each letter in even position (the first character is in position 0),
    reverse the whole result.

#Example:

your text: "BORN IN 2015!", shift 1

1 + 2 + 3 -> "CPSO JO 7984!"

4 "CpSo jO 7984!"

5 "!4897 Oj oSpC"
'''


def play_pass(s, n):
    # ord: a-z = 97-122, A-Z = 65-90, 0-9 = 48-57
    result = []
    for char in map(ord, s):        
        if 97<=char<=122 or 65<=char<=90:
            if char < 97:
                char += 32
            t = 97 + (char-97+n)%26
        elif 48 <= char <= 57:            
            t = 48 + (57-char)%57
        else:
            t = char     
        result.append(chr(t))
    res = ''.join(x.upper() if i%2==0 else x.lower() for i,x in enumerate(result))
    return res[::-1]
