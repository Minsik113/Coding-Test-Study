s = input()
dict_d = {
    'a':1
    ,'b':2
    ,'c':3
    ,'d':4
    ,'e':5
    ,'f':6
    ,'g':7
    ,'h':8
}
# 북오른쪽부터 clockwise
dx = [1,2,2,1,-1,-2,-2,-1]
dy = [-2,-1,1,2,2,1,-1,-2]
x = dict_d[s[0]]-1
y = int(s[1])-1

# map
arr = [[0 for _ in range(8)] for _ in range(8)]

ans = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or ny < 0 or nx >= 8 or ny >= 8:
        continue
    ans += 1
print(ans)