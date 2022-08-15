'''
날짜: 2022. 08. 13
시간복잡도:

문제:
풀이: 어렵; 이해하는게 어렵네. 

0,0 0,1 0,2
1,0 1,1 1,2
2,0 2,1 2,2

'''
n, m = map(int, input().split())
x, y, d = map(int,input().split())
ans = 1 # 방문한 육지 수. 시작시 방문하니까 1로시작
count = 0 # 오류 횟수 세기위한 변수

# 맵생성 육지(0),바다(1),가봄(2)
arr = [list(map(int, input().split())) for _ in range(n)] 
arr[x][y] = 2

dx = [0, -1, 0, 1] # 바라보는방향 "북 동 남 서"
dy = [-1, 0, 1, 0] # -> 사실은 "서 북 동 남"

def turn_left(direct):
    direct -= 1
    if direct < 0:
        direct = 3
    return direct 
def turn_right(direct):
    direct += 1
    if direct == 4:
        direct = 0
    return direct 
while True:
    # 종료조건
    if count == 4:
        # 4번다봤으면 현재위치에서 그대로 후진 
        d = turn_right(d)
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] == 1: # 바다 라면 -> 종료
            break
        else: # 바다가 아니라면 -> 좌표변경count초기화
            x = nx
            y = ny
            count = 0 # 아래이미있음
    
    nx = x + dx[d] # 이동했을때 좌표
    ny = y + dy[d]
    d = turn_left(d) # 왼쪽으로돌기 # 방향전환하고 땅을 확인하는거라서 무조건 돌긴해야함.

    print(f'현위치 {x},{y} -> {nx},{ny}', end=' ')
    # 맵을 벗어남, 가본곳, 바다 -> 왼쪽으로돌기, 카운트증가
    if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] == 2 or arr[nx][ny] == 1:
        count += 1 # 카운트증가
        print(f' 못가는곳이니까 돌자',end='\n')
    # 안가본곳이라면 -> 가봤다고 체크, 현재좌표 변경
    else:
        arr[nx][ny] = 2
        ans += 1
        x, y = nx, ny
        count = 0 # 새로운 땅이니 카운트 초기화
        print(f' 방문~',end='\n')
print(arr)
print(ans)

#############################################
#############################################
# n, m = map(int, input().split())
# x, y, d = map(int,input().split())
# ans = 0

# # 맵생성 육지(0),바다(1),가봄(2)
# arr = [list(map(int, input().split())) for _ in range(n)] 
# arr[x][y] = 2

# # 왼쪽으로 돌기
# def turn_left(direct):
#     direct -= 1
#     if direct < 0:
#         direct = 3
#     return direct
# def turn_right(direct):
#     direct += 1
#     if direct > 3:
#         direct = 0
#     return direct
# # direct가 '북(0)'이면 '서'로 이동이니까  dx,dy를 서북동남으로 선언
# dx = [-1, 0, 1, 0] # 방위 서     북    동     남  으로이동
# dy = [0, 1, 0, -1] # -> 원래북 원래동 원래남 원래서

# flag = True
# count = 0
# while flag:
#     # 종료조건 만들자
#     if count == 4: # count=4 -> 현재 방향 유지 + 뒤로후진
#         # 나한테는 이게 현재 바라보는 방향임
#         d = turn_right(d)
#         d = turn_right(d) # 나느 이래야 현재 바라보는 방향에서 후진임.

#         nx = x + dx[d]
#         ny = y + dx[y]
#         if arr[nx][ny] == 1: # 바다라면 종료
#             flag = False
#         else: # 육지(0) or 가본길(2) -> 방향유지한채 뒤로이동
#             x = nx
#             y = ny
#             count = 1 # 원래있던길은 이미 방문한거니까
    
#     for i in range(4):
#         nx = x + dx[d]
#         ny = y + dy[d]
#         # 벗어나면 안되고, 바다(1) or 이미본경우(2) -> 카운트증가 + 회전해야함.
#         if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] == 1 or arr[nx][ny] == 2: 
#             count += 1
#             d = turn_left(d) # 방향바꿈
#         # 안가본 곳이면 -> 가고 + 회전해야함
#         else:
#             arr[x][y] = 2 # 서있던 위치는 방문했다고 체크하고
#             x, y = nx, ny # 내위치 위치 이동하고
#             count = 0
#             ans += 1
#             d = turn_left(d) # 방향바꿈
#             break
# print(arr)
# print(ans)

##################################################
##################################################
# n, m = map(int, input().split())
# x, y, d = map(int,input().split())
# ans = 0

# # 맵생성 육지(0),바다(1),가봄(2)
# arr = [list(map(int, input().split())) for _ in range(n)] 
# arr[x][y] = 2

# # 왼쪽으로 돌기
# def turn_left(direct):
#     direct -= 1
#     if direct < 0:
#         direct = 3
#     return direct
# def turn_right(direct):
#     direct += 1
#     if direct > 3:
#         direct = 0
#     return direct
# # direct가 '북(0)'이면 '서'로 이동이니까  dx,dy를 서북동남으로 선언
# dx = [-1, 0, 1, 0] # 방위 서     북    동     남  으로이동
# dy = [0, 1, 0, -1] # -> 원래북 원래동 원래남 원래서

# flag = True
# count = 0
# while flag:
#     # 종료조건 만들자
#     if count == 4: # count=4 -> 현재 방향 유지 + 뒤로후진
#         # 나한테는 이게 현재 바라보는 방향임
#         d = turn_right(d)
#         d = turn_right(d) # 나느 이래야 현재 바라보는 방향에서 후진임.

#         nx = x + dx[d]
#         ny = y + dx[y]
#         if arr[nx][ny] == 1: # 바다라면 종료
#             flag = False
#         else: # 육지(0) or 가본길(2) -> 방향유지한채 뒤로이동
#             x = nx
#             y = ny
#             count = 1 # 원래있던길은 이미 방문한거니까
    
#     for i in range(4):
#         nx = x + dx[d]
#         ny = y + dy[d]
#         # 벗어나면 안되고, 바다(1) or 이미본경우(2) -> 카운트증가 + 회전해야함.
#         if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] == 1 or arr[nx][ny] == 2: 
#             count += 1
#             d = turn_left(d) # 방향바꿈
#         # 안가본 곳이면 -> 가고 + 회전해야함
#         else:
#             arr[x][y] = 2 # 서있던 위치는 방문했다고 체크하고
#             x, y = nx, ny # 내위치 위치 이동하고
#             count = 0
#             ans += 1
#             d = turn_left(d) # 방향바꿈
#             break
# print(arr)
# print(ans)


