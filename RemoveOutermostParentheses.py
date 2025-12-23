def removeOuterParentheses(s):
    res = ""
    bal = 0
    for c in s:
        if c == '(':
            if bal > 0:
                res += c
            bal += 1
        else:
            bal -= 1
            if bal > 0:
                res += c
    return res
