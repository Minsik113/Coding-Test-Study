# p.363 카드 정렬하기

# 정렬 해서 앞에서 부터 2개씩 더한 총계를 구하면 될 것 같음

N = int(input())

numbers = []
for _ in range(N):
    tmp = int(input())
    numbers.append(tmp)

answer = []
for i in range(N):
    if i == 0:
        continue
    elif i == 1:
        tmp = numbers[i-1] + numbers[i]
    else:
        tmp = answer[i-2] + numbers[i]
    answer.append(tmp)

print(sum(answer))

