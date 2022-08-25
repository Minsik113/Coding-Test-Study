'''
날짜: 2022. 08. 26
시간복잡도:

문제:
풀이: 시작점부터 bfs로 이동. 갈수있는 칸에 초를 적는다
01:38~01:52
'''
from collections import deque

def bfs(arr, x, y, ans):
    q = deque()
    q.append([x,y,1]) # 좌표,이동횟수
    arr[x][y] = 2 # 방문 체크
    while q:
        a, b, c = q.popleft()
        if a == n-1 and b == m-1: # 한칸씩 움직이니까 제일 먼저발견되는게 빠른거임.
            ans = min(ans,c)
            break
        print(f'{a},{b},{c}')
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = 2 # 방문했다고체크
                q.append([nx,ny,c+1])
    return ans                

n, m = map(int, input().split())
arr = []
dx = [-1,0,1,0] # 북동남서
dy = [0,1,0,-1]
for i in range(n):
    arr.append(list(map(int, input())))

ans = bfs(arr, 0, 0, 1e9) # 배열 안넘겨도됨. 1e9도 bfs안에서 써도됨
print(ans)