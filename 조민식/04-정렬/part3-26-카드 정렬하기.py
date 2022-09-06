'''
날짜: 2022. 09. 06
시간복잡도:

문제:
풀이:
02:07 ~ 02:15

n = 10만 -> O(NlogN)

그냥 작은애들끼리 계속 합하면 되는거아닌가?
1. 제일작은거 2개 추출 후 덧셈. 
2. 나온 값 저장 후 리스트에 넣는다.
3. 1,2번 반복
4. 1개 나오면 종료

heap 쓰면될듯?
'''

import sys, heapq
input = sys.stdin.readline

n = int(input())
q = []
ans = 0
# 1. 입력
for _ in range(n):
    heapq.heappush(q, int(input()))

while True:
    # 종료조건 -> 개수 1개면 종료, 입력이 0일수도 있으니 등호추가
    if len(q) <= 1:
        break
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    temp = a+b
    ans += temp
    heapq.heappush(q, temp)

print(ans)