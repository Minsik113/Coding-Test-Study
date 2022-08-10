# 수행 시간 측정
import time
start_time = time.time() # 측정 시작

price = int(input('거스름돈을 입력하세요.'))
count = 0 # 초기화

coins = [500, 100, 50, 10] # 동전 종류 지정

for i in coins:
    tmp = price // i # 코인 개수
    count += tmp
    price = price % i

print(count)

end_time = time.time() # 측정 종료
print('time :', end_time - start_time) # 수행 시간 출력