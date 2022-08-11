# 2. 곱하기 혹은 더하기
number = input()

result = int(number[0])

for i in range(1, len(number)):
    n = int(number[i])
    if n < 1 or result <=1 :
        result += n
    else:
        result *= n

print(result)

