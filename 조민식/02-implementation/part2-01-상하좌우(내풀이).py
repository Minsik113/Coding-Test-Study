'''
날짜: 2022. 08. 13
시간복잡도: O(N^2)

문제: 
풀이: 
dictionary써서접근 방향많아질수록 책보단빠를듯?
'''
n = int(input())
directs = list(input().split())

dict_d = {
    'U':0
    ,'R':1
    ,'D':2
    ,'L':3
}
# 이 문제에서 (1,1)에서 북으로가면 (0,1)이됨. 
dx = [-1, 0, 1, 0] # 북 동 남 서 
dy = [0, 1, 0, -1] 

# map 생성
arr = [[0 for _ in range(n)] for _ in range(n)] # O(N^2)

x, y = 0, 0  
for direct in directs:
    vx = x + dx[dict_d[direct]]
    vy = y + dy[dict_d[direct]]
    # 밖으로 나간다면 무시
    if vx < 0 or vy < 0 or vx >= n or vy >= n:
        continue
    # 안나가면 위치변경
    x = vx
    y = vy
print(x+1, y+1)




