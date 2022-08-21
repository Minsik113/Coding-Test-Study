# 럭키 스트레이트
N = int(input())

# 오른쪽부터 3개씩 나누면 자릿수
list_a, list_b, list_c = [[],[],[]]
N = list(map(int, str(N)))

# 자릿수에 따라 케이스 지정
# 3자리 이하인 경우 --> ready 반환
if len(N) <= 3:
    result = 'READY'
# 3~6자리인 경우 -> 오른쪽부터 3자리, 나머지를 비교
elif len(N) <= 6:
    list_a = N[-3:]
    del N[-3:]
    list_b = N
    result = sum(list_a) == sum(list_b)
# 7자리 이상인 경우 -> 오른쪽부터 3자리, 4~6자리, 나머지를 비교
else:
    list_a = N[-3:]
    list_b = N[-6:-3]
    del N[-6:]
    list_c = N
    result = sum(list_a) == sum(list_b) == sum(list_c)

# 결과에 따라 lucky 또는 ready 반환
if result == True:
    print('LUCKY')
else:
    print('READY')