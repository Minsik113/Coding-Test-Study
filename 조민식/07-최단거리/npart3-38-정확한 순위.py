'''
날짜: 2022.10.14
시간복잡도:

문제:
풀이:
15:08 ~ 

a번학생에서 b번학생으로 연결이 될 수 있는지를 파악하면된다.
전체적으로 a번학생이 모든학생들까지 갈 수 있는지 판단.
하나라도 못 가면 안됨.
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[1e9]*(n+1) for _ in range(n+1)]
# 1. 자기자신으로 가는건 없음
for i in range(1, n+1):
    graph[i][i] = 0
# 2. 간선입력받음
for _ in range(m):
    l, h = map(int,input().split()) # 낮은애 높은애
    graph[l][h] = 1
# 3. 플로이드 워셜
for k in range(1, n+1): # 거쳐가는 노드
    for i in range(1, n+1): # 시작 노드
        for j in range(1, n+1): # 도착 노드
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
ans = 0

for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if graph[i][j] != 1e9 or graph[j][i] != 1e9:
            cnt += 1
    if cnt == n:
        ans += 1
print(ans)