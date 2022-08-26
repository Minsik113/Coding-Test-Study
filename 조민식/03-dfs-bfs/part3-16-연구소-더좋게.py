'''
날짜: 2022. 08. 26
시간복잡도:

문제:
풀이: 0 위치에 벽 3개 세운다
13:49 ~ 14:10
0: 빈칸
1: 벽
2: 바이러스
'''
from itertools import combinations
from collections import deque
import sys
import copy

def bfs(arr, i, j):
    q = deque()
    q.append([i,j])
    while q:
        kx, ky = q.popleft()
        for i in range(4):
            nx = kx + dx[i]
            ny = ky + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = 2 # 바이러스 퍼짐
                q.append([nx,ny])

    return arr

input = sys.stdin.readline
# 1.맵 생성
n, m = map(int, input().split())
arr_raw = []
possible_pos = [] # 빈칸들 좌표. 벽 세울 수 있는 위치
virus_pos = [] # 바이러스 좌표
ans = -1
# 2. 벽돌 생성될 수 있는 좌표 넣기
for i in range(n):
    t = list(map(int, input().split()))
    arr_raw.append(t)
    for j in range(m):
        if t[j] == 0: 
            possible_pos.append([i,j])
        if t[j] == 2:
            virus_pos.append([i,j])
            
# 3.벽돌넣기
dx = [-1, 0, 1, 0] # 북동남서
dy = [0, 1, 0, -1]
aaa = 0
for v1,v2,v3 in combinations(possible_pos, 3):
    arr = copy.deepcopy(arr_raw) # 초기화
    # 3-1. 벽돌 세우기
    arr[v1[0]][v1[1]] = 1
    arr[v2[0]][v2[1]] = 1
    arr[v3[0]][v3[1]] = 1
    
    # 3-2. 바이러스 퍼트리기
    for i, j in virus_pos:
        arr = bfs(arr, i, j)

    # 3-3. 안전구역 수 세기
    temp = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0: # 안전구역이면
                temp += 1
    ans = max(ans, temp)
print(ans)

