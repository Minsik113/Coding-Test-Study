'''
날짜: 2022. 09. 18
시간복잡도:

문제:
풀이:
21:40 ~ 21:50

1. -1한 정보 저장
2. 나눌 수 있으면 나눈 정보도 저장
bfs

테스트값
1234567 
= 17
-> 0.00595 sec

'''
from collections import deque

def bfs(x):
    res = 0
    q = deque()
    q.append([x, 0])
    
    while q:
        nx, cnt = q.popleft()
        # 1. 종료조건
        if nx == 1:
            res = cnt
            break
        # 2. 나누기 가능하면 추가
        if nx % 5 == 0:
            q.append([nx//5,cnt+1])
        elif nx % 3 == 0:
            q.append([nx//3,cnt+1])
        elif nx % 2 == 0:
            q.append([nx//2,cnt+1])
        # 3. 뺀거는 무조건 추가
        q.append([nx-1,cnt+1])

    return res

n = int(input())

import time
start = time.time()
print(bfs(n))
end = time.time()
print(f"{end - start:.5f} sec")
