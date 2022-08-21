# 문자열 재정렬
# 알파벳 만나면 정렬, 숫자 만나면 합

S = input()
digit = 0
result = ''

for i in S:
    try:
        digit += int(i)
    except:
        result += i
result = ''.join(sorted(result))
print(result+str(digit))