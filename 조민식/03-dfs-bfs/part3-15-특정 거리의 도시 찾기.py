'''
날짜: 2022. 08. 26
시간복잡도:

문제:
풀이: x부터 bfs로 모든 노드 걸리는 시간 잰다. 마지막에 K시간만큼 걸린애들만 출력
12:53 ~ 13:15
'''
from collections import deque
import sys
input = sys.stdin.readline

def bfs(arr, start, dist):
    q = deque()
    q.append([start,-1]) # 시작노드, 시작노드부터 걸린 거리
    while q:
        v, c = q.popleft()
        # 안본 곳이라면 들어가서 연결된애들 값추가하고 q에 넣어봐야지
        if dist[v] == -1:
            dist[v] = c+1 # 방문체크하고
            for i in range(len(arr[v])):
                q.append([arr[v][i],c+1]) # 연결된 애들 넣어본다

n, m, k, start = list(map(int, input().split()))
# 1. 맵 생성
arr = [[] for _ in range(n+1)]
dist = [-1] * (n+1) # 방문체크
# 2.길 연결
for i in range(m):
    a, b = map(int, input().split()) # a-b
    arr[a].append(b) # 길 연결

bfs(arr, start, dist)
# 출력
res = []
for i in range(1, len(dist)):
    if dist[i] == k:
        res.append(i)
res = sorted(res)
# print(res)
if len(res)==0: # 도시 없으면 -1
    print(-1)
else:
    for i in res: # 도시 있으면 오름차순으로 출력
        print(i)


