s = "python is awesome"
result = ""

for i in range(len(s)):
    if i == 0 or s[i-1] == " ":
        result += s[i].upper()
    else:
        result += s[i]

print(result)
