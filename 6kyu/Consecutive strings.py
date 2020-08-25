'''
You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.
Example:

longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
Note

consecutive strings : follow one after another without an interruption

'''

def longest_consec(strarr, k):
    if len(strarr) >= k > 0 and strarr:
        r = {}
        for i,word in enumerate(strarr, k):
            wordslen = sum(len(x) for x in strarr[i-k:i])
            if wordslen not in r:
                r[wordslen] = i-k
        m = r[max(r)]
        return ''.join(strarr[m:k+m])  
    return ""
