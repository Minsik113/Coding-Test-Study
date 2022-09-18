'''
날짜:
시간복잡도:

문제:
풀이:

테스트값
2 10000
3
5
->2000
8.46564 sec

'''
import time
start = time.time()

n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))

# 결과 저장 리스트
d = [10001] * (m+1) # 최대값 m이니까

d[0] = 0

for i in range(n):
    for j in range(arr[i], m+1):
        if d[j - arr[i]] != 10001: # i-k원을 만드는 경우가 존재한다면
            d[j] = min(d[j], d[j-arr[i]]+1)

if d[m] == 10001:
    print(-1)
else: 
    print(d[m])
end = time.time()
print(f"{end - start:.5f} sec")