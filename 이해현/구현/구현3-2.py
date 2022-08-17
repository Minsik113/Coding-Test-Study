# 3-2 : 문자재정렬
s = input()

alpha, num = [],[]
for i in range(len(s)):
    if s[i].isnumeric():
        num.append(s[i])
    else:
        alpha.append(s[i])

result = ''.join(sorted(alpha)+sorted(num))

print(result)
