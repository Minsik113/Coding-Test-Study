import sys
input = sys.stdin.readline

n = int(input()) 
arr = []
# 1. 맵입력
for i in range(n):
    arr.append(list(map(int,input().split())))
# 2. 숫자 쌓기
for i in range(1, n):
    for j in range(i+1):
        # 0열이면 
        if j==0: 
            arr[i][0] = arr[i-1][0] + arr[i][0]
        # 맨 끝열이면
        elif i==j:
            arr[i][j] = arr[i-1][j-1] + arr[i][j]
        # 중간이면
        else:
            arr[i][j] = max(arr[i-1][j-1], arr[i-1][j]) + arr[i][j]
print(max(arr[n-1]))