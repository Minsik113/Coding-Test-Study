'''
날짜: 2022.10.11
시간복잡도: O(N^3)

문제: https://www.acmicpc.net/problem/11404
풀이: 
16:20 ~ 16:33

한 도시에서 출발하여 여러 도시로 이동. 최소비용으로 이동 -> 플로이드워셜 혹은 다익스트라
n이 100이하이므로 O(N^3)가능

'''
import sys
input = sys.stdin.readline

n = int(input()) # 도시 개수
m = int(input()) # 경로 수

# 1. 도시마다의 최소 거리 저장하는 2차원 리스트 생성
graph = [[1e9]*(n+1) for _ in range(n+1)] # 2차원 배열. 도시마다 거리 저장
for i in range(1, n+1):
    graph[i][i] = 0 # 자기 자신은 못 감

# 2. 경로 입력
for _ in range(m): 
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b],c)

# 3. 플로이드 워셜 알고리즘
for k in range(1, n+1): # 중간 도시
    for i in range(1, n+1): # 출발 도시
        for j in range(1, n+1): # 도착 도시
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    # print('>>')
# 4. 결과
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] >= 1e9:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print(end='\n')
