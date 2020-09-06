'''
Your job is to create a calculator which evaluates expressions in Reverse Polish notation.

For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.

For your convenience, the input is formatted such that a space is provided between every token.

Empty expression should evaluate to 0.

Valid operations are +, -, *, /.

You may assume that there won't be exceptional situations (like stack underflow or division by zero).
'''

'''
#v1
def calc(expr):    
    exprlist = expr.split()
    while exprlist:
        for i,x in enumerate(exprlist):
            if x in ['+', '-', '*', '/']:
                if x == '+':
                    t = float(exprlist[i-2]) + float(exprlist[i-1])
                if x == '-':
                    t = float(exprlist[i-2]) - float(exprlist[i-1])
                if x == '*':
                    t = float(exprlist[i-2]) * float(exprlist[i-1])
                if x == '/':
                    t = float(exprlist[i-2]) / float(exprlist[i-1])
                exprlist[i-2: i+1] = [t]
                break
            if len(exprlist) == 1:
                return float(exprlist[0])
    return 0
'''

#v2
import operator
def calc(expr):
    operators = {'+': operator.add,'-': operator.sub,'*': operator.mul,'/': operator.truediv}
    cache = [0]
    exprlist = expr.split()
    for x in exprlist:
        if x in operators:
            b, a = cache.pop(), cache.pop()
            cache.append(operators[x](a, b))
        elif x:
            cache.append(float(x))
    return cache.pop()
