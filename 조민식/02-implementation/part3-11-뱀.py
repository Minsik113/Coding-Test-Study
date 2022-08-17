'''
날짜: 2022. 08. 17
시간복잡도: 완전탐색

문제:
풀이: linkedlist로 풀면 쉬울거같은데
18:47~19:55 ㅡㅡ..
'''
from collections import deque

n = int(input()) # NxN 맵
k = int(input()) # 사과 개수

pos_apple = [list(map(int,input().split())) for _ in range(k)]
print(pos_apple)

d = int(input()) # 방향전환 횟수
change_direct = deque()
for _ in range(d):
    a, b = input().split()
    change_direct.append([int(a), b])
print(change_direct)

# [함수 1] - 방향전환
def turn_direct(c, d): # 방향, 현재방향
    if c == 'D': # 오른쪽으로 90도 turn_right
        d += 1
        if d == 4:
            d = 0
    elif c == 'L': # 왼쪽으로 90도 turn_left
        d -= 1
        if d == -1:
            d = 3
    return d

# 1.맵 생성 0(땅), 1(사과), 자기몸(2)
arr = [[0 for _ in range(n)] for _ in range(n)]
for a, b in pos_apple:
    arr[a-1][b-1] = 1

now_time = 0 # 지금까지의 초
x, y = 0,0 # 시작하는 곳 (0,0)
arr[x][y] = 2 # 시작하는 곳은 뱀이 위치함
snake = deque() # 뱀 정보
snake.append((0,0))

dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1] # x는 행, y는 열
d = 1 # 처음에 동쪽방향시작 idx=1
# 2.종료조건: 벽만나거나, 자기자신과부딪힘
print('맵',arr)
while True:
    now_time += 1 # 4-5.현재까지의 시간 +1초
    # 3. 벽 or 자기자신 만나면 종료    
    nx = x + dx[d]
    ny = y + dy[d]
    print(f'time:{now_time}, nx:{nx}, ny:{ny}, d:{d}')
    if nx < 0 or ny < 0 or nx >= n or ny >= n or arr[nx][ny] == 2:
        break
    # 4. 이동 / 사과 유무 체크
    snake.append((nx,ny)) # 4-1. 뱀 이동
    if arr[nx][ny] == 0: # 4-2. 사과X -> 단순이동
        a, b = snake.popleft() 
        arr[a][b] = 0
    arr[x][y] = 2 # 4-3.현재위치 땅(0)->뱀(2) 으로 변경
    x, y = nx, ny # 4-4.내좌표 변경 x,n -> nx,ny
    print(f'snake:{snake}')
    # print(f'변경된 맵 {arr}')

    # 5. 초가 끝난 후, 방향 전환할게 남아있다면 변경
    if change_direct and change_direct[0][0] == now_time:
        t, direct = change_direct.popleft()
        d = turn_direct(direct, d) # 방향전환 

print(now_time)