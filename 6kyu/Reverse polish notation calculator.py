'''
Your job is to create a calculator which evaluates expressions in Reverse Polish notation.

For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.

For your convenience, the input is formatted such that a space is provided between every token.

Empty expression should evaluate to 0.

Valid operations are +, -, *, /.

You may assume that there won't be exceptional situations (like stack underflow or division by zero).
'''

def calc(expr):    
    def dig(n):
        if isinstance(n, str):
            try:
                return int(n)
            except:
                return float(n)
        return n    
    exprlist = expr.split()
    while exprlist:
        for i,x in enumerate(exprlist):
            if x in ['+', '-', '*', '/']:
                if x == '+':
                    t = dig(exprlist[i-2]) + dig(exprlist[i-1])
                if x == '-':
                    t = dig(exprlist[i-2]) - dig(exprlist[i-1])
                if x == '*':
                    t = dig(exprlist[i-2]) * dig(exprlist[i-1])
                if x == '/':
                    t = dig(exprlist[i-2]) / dig(exprlist[i-1])
                exprlist[i-2: i+1] = [t]
                break
            if len(exprlist) == 1:
                return dig(exprlist[0])
    return 0
