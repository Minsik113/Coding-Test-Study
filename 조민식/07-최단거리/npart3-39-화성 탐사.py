'''
날짜:
시간복잡도:

문제:
풀이:

''''''
날짜: 2022.10.11
시간복잡도:

문제:
풀이:
18:00 ~ 

DP
d[i][j] = min(d[i][j], d[i-1][j]+ori[i][j], d[i][j-1]+ori[i][j])

테스트케이스
2
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4

'''
import sys
input = sys.stdin.readline

t = int(input())
for test in range(t):
    n = int(input())
    ori = []
    # 1. 맵 입력받기
    for _ in range(n):
        ori.append(list(map(int, input().split())))
    # 2. dp맵 카피
    dp = [[1e9]*n for _ in range(n)]
    dp[0][0] = ori[0][0]

    print(">>")
    print(ori)
    
    dx = [-1,0,1,0] # 북동남서
    dy = [0,1,0,-1]

    # 2. 이동
    for i in range(n):
        for j in range(n):

            for x in range(4):
                nx = i + dx[x]
                ny = j + dy[x]
                if nx < 0 or ny < 0 or nx >=n or ny >= n:
                    continue
                dp[i][j] = min(dp[i][j], dp[nx][ny]+ori[i][j])
    print('sss')
    print(dp)
