# 수행 시간 측정
import time
start_time = time.time() # 측정 시작

coins = [500, 100, 50, 10] # 동전 종류 지정
quant = [] # 동전 개수를 담는 리스트
price = int(input('거스름돈을 입력하세요.'))

for i in coins:
    tmp = price // i # 코인 개수
    quant.append(tmp) # 리스트에 추가
    price = price % i

print('{}원 동전 {}개, {}원 동전 {}개, {}원 동전 {}개, {}원 동전 {}개'.format(
    coins[0], quant[0], coins[1], quant[1], coins[2], quant[2], coins[3], quant[3]))

end_time = time.time() # 측정 종료
print('time :', end_time - start_time) # 수행 시간 출력