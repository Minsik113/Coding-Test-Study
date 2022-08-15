n = int(input())
directs = list(input().split())

# 이 문제에서 (1,1)에서 북으로가면 (0,1)이됨. 
dx = [-1, 0, 1, 0] # 북 동 남 서 
dy = [0, 1, 0, -1] 
list_d = ['U','R','D','W']

# map 생성
arr = [[0 for _ in range(n)] for _ in range(n)]

x, y = 1, 1
for direct in directs:
    for i in range(len(list_d)):
        if direct == list_d[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        # 밖으로 나간다면 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        # 안나가면 위치변경
    x, y = nx, ny 
print(x, y)




