# Q3. 문자열 뒤집기
import time
start_time = time.time() # 측정 시작

S = input('숫자로 이루어진 문자열을 입력하세요 ->') # 문자열

# 0을 1으로 바꾸는 변수 change_to_one
# 1을 0로 바꾸는 변수 change_to_zero

change_to_zero = 0
change_to_one = 0

if S[0] == '0':
    change_to_one = change_to_one + 1
else:
    change_to_zero = change_to_zero + 1

for i in range(len(S)-1):
    if S[i] == S[i + 1]:
        continue
    else:
        if S[i+1] == '0':
            change_to_one = change_to_one + 1
        else:
            change_to_zero = change_to_zero + 1

print(min(change_to_zero, change_to_one))

end_time = time.time() # 측정 종료
print('time :', end_time - start_time)

