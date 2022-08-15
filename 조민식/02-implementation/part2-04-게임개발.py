'''
날짜: 2022. 08. 13
시간복잡도:

문제:
풀이:
'''




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


