'''
날짜:2022. 09. 22
시간복잡도:

문제:https://www.acmicpc.net/problem/1932
풀이:
23:32 ~ 

n = 500이니까 n^2이어도 25000임

d[i][0] = d[i-1][0]+d[i][0]
d[i][n] = max(d[i-1][n-1]+d[i][0], d[i-1][n]+d[i][0])

5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
'''
import sys
input = sys.stdin.readline

n = int(input()) 
arr = []
d = [[0]*n for _ in range(n)]
# 1. 맵입력
for i in range(n):
    b = list(map(int,input().split()))
    arr.append(b)
# 2. 맨위에꺼 입력
d[0][0] = arr[0][0]
for i in range(1, n):
    for j in range(i+1):
        # 0열이면 
        if j==0: 
            d[i][0] = d[i-1][0]+arr[i][0]
        else:
            d[i][j] = max(d[i-1][j-1], d[i-1][j]) + arr[i][j]

print(max(d[n-1]))