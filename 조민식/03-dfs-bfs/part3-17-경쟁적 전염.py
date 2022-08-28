'''
날짜: 2022. 08. 28
시간복잡도:

문제:
풀이:
20:06 ~ 20:44
'''
from collections import deque
import sys

def bfs(pos_virus, s):
    q = deque(pos_virus) # 이렇게안하고 따로 append해주면 []가 하나 더생김
    while q:
        virus, now_time, x, y = q.popleft()
        # 종료조건
        if now_time > s:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 바이러스 점염. 주변지역이 0이면 감염시켜라
            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y]
                q.append([virus,now_time+1,nx,ny])

input = sys.stdin.readline
pos_virus = []

n, k = map(int, input().split()) # nxn, 바이러스개수: k
arr = []

# 1. 맵 입력
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
    for j in range(n): # 바이러스 좌표 입력
        if temp[j] != 0:
            pos_virus.append([temp[j],1,i,j]) # 바이러스 번호, 0초, x, y 
    
s,ax,ay = map(int, input().split()) # s초뒤에 (x,y)좌표의 바이러스 출력
ax = ax-1 # 내가만들 맵은 (0,0)부터 시작이므로
ay = ay-1
dx = [-1,0,1,0] # 북동남서
dy = [0,1,0,-1]

end_time = 1
pos_virus = sorted(pos_virus,key=lambda x:x[0]) # 바이러스 번호순서대로 정력

# 2. 바이러스 전파
bfs(pos_virus, s)
print(arr[ax][ay])

