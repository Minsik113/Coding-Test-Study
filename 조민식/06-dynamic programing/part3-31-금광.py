'''
날짜: 2022. 09. 19
시간복잡도:

문제:
풀이:
00:40 ~ 01:02

arr[i][j] = i행 j열에 존재하는 금의 양
df[i][j] = i행 j열까지의 최적의 해

테스트 값
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
'''
import sys
input = sys.stdin.readline

t = int(input())
# n번 실행
for _ in range(t):
    n, m = map(int, input().split())
    arr = [] # 금광저장

    # 1. 금광 맵 설정
    temp = list(map(int, input().split()))
    for i in range(0, len(temp), m):
        arr.append(temp[i:i+m])
    
    # 2. 이동 
    for i in range(1,m): # 열 -> column으로 봐야함
        for j in range(n): # 행
            # 2-1.맨위 -> 앞 아래
            if j==0:
                arr[j][i] = max(arr[j][i-1], arr[j+1][i-1]) + arr[j][i]
            # 2-2.맨아래 -> 앞 위
            elif j==(n-1):
                arr[j][i] = max(arr[j][i-1], arr[j-1][i-1]) + arr[j][i]
            # 2-3.중간 ->  위 앞 아래
            else:
                arr[j][i] = max(arr[j-1][i-1], arr[j][i-1], arr[j+1][i-1]) + arr[j][i]
    
    res = 0
    for i in range(n):
        res = max(res, arr[i][m-1]) # 마지막열중에 제일큰거
    print(arr)
    print(res)




