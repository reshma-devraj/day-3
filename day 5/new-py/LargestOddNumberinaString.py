def largestOddNumber(s):
    for i in range(len(s)-1, -1, -1):
        if int(s[i]) % 2:
            return s.lstrip('0')[:i+1]
    return ""
