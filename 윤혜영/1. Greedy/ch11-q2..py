# Q2. 곱하기 혹은 더하기
import time
start_time = time.time() # 측정 시작

S = '20984'
S_list = list(S)
cal_list = list('*'.join(S_list)) # 모두 곱으로 연결한 리스트 생성

for i in cal_list: # 왼쪽부터 문자열 확인
    if i == '0':
        cal_list[cal_list.index(i)-1] = '+'
        cal_list[cal_list.index(i)+1] = '+'
    else:
        continue
print(cal_list)

# 연산하는 함수 (+, *)
def cal_twokind(list):
    result = 0
    for i in list:
        if list.index(i) == 0:
            continue
        elif list.index(i) == 1:
            if i == '+':
                tmp = int(list[list.index(i) - 1]) + int(list[list.index(i) + 1])
            elif i == '*':
                tmp = int(list[list.index(i) - 1]) * int(list[list.index(i) + 1])
            result = tmp
            print('인덱스는', list.index(i), 'i는', i, 'result는',result)
        elif list.index(i) > 1:
            if i == '+':
                result = result + int(list[list.index(i) + 1])
                print('인덱스는', list.index(i), 'i는', i, 'result는',result)
            elif i == '*':
                result = result * int(list[list.index(i) + 1])
                print('인덱스는', list.index(i), 'i는', i, 'result는',result)
            else:
                continue

cal_twokind(cal_list)

end_time = time.time() # 측정 종료
print('time :', end_time - start_time)