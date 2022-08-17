# 3-1 : 럭키 스트레이트

n = input() #입력받는 숫자 문자열
sum = 0

#가운데 인덱스 기준 왼쪽 숫자는 더함
for i in range(len(n)//2):
    sum += int(n[i])
#가운데 인덱스 기준 오른쪽 숫자는 뺌
for i in range(len(n)//2):
    sum -= int(n[i])

#sum의 값이 0이 나오면 럭키스트라이크현
if sum == 0:
    print('LUCKY')
else :
    print('READY')
