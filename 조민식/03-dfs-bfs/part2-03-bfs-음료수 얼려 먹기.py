'''
날짜: 2022. 08. 25
시간복잡도:

문제:
풀이: bfs로 하나씩보자
생각하고풀자 좀
'''
from collections import deque

def bfs(arr, a, b, visited):
    q = deque()
    # 값넣고
    q.append([a,b])
    # 방문확인
    visited[a][b] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 벗어나면 나감
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 봐야하고 방문안했다면 봐라
            if arr[nx][ny]==0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append([nx, ny])

n, m = map(int, input().split())
arr = []
visited = [[False]*m for _ in range(n)]
for i in range(n):
    arr.append(list(map(int, input())))
    
ans = 0
dx = [-1, 0, 1, 0] # 북동남서
dy = [0, 1, 0, -1]
# 배열, 시작좌표, 그룹개수
# bfs(arr, 1,2, visited)
for i in range(n):
    for j in range(m):
        # 봐야하는 곳이면서 방문안한곳일 때 돌자.
        if arr[i][j]==0 and not visited[i][j]:
            bfs(arr, i, j, visited)
            ans += 1
print(ans)