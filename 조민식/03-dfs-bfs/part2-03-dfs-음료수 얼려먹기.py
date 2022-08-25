def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if arr[x][y] == 0:
        arr[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))
    
ans = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            ans += 1

print(ans)