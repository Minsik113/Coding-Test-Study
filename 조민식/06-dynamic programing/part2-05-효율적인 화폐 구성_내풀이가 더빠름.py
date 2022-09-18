'''
날짜: 2022.09.18 
시간복잡도:

문제:
풀이:
23:23 ~ 23:43

비싼 동전이 많이 사용될수록 효율적이다.

테스트값
2 10000
3
5
->2000
1.59961 sec
'''
import time
start = time.time()

n, m = map(int, input().split())
arr = [1e9] * (m+1)

for _ in range(n): 
    coin = int(input())
    num = 1
    # 예외처리) 목표한 값보다 더 큰 동전은 사용안해도됨
    if coin > m:
        continue
    
    # 1.시작하는 건 코인1개
    arr[coin] = 1
    # 2.이후 코인은 (현재값, 이전꺼+1) 비교
    while coin*num <= m:
        temp = coin*num 
        arr[temp] = min(arr[temp], arr[temp-coin]+1) # 자기자신이랑 이전
        num += 1

if arr[m] == 1e9:
    print(-1)
else:
    print(arr[m])
end = time.time()
print(f"{end - start:.5f} sec")



