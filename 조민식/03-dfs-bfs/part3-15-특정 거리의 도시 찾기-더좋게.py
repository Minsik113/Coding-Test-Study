'''
날짜: 2022. 08. 26
시간복잡도:

문제:
풀이: x부터 bfs로 모든 노드 걸리는 시간 잰다. 마지막에 K시간만큼 걸린애들만 출력
12:53 ~ 
'''
from collections import deque
import sys
input = sys.stdin.readline

def bfs(res, start, visited):
    q = deque()
    q.append([start,0]) # 시작노드, 시작노드부터 걸린 거리
    visited[start] = True # 현재노드 방문체크

    while q:
        v, c = q.popleft()
        # 종료조건
        if c > k: # bfs니까 하나라도 나오면 종료됨
            break
        # 정답넣기
        if c == k:
            res.append(v)
        # 안본 곳이라면 -> 연결된애들 값추가하고 q에 넣어봐야지
        for i in arr[v]:
            if not visited[i]:
                visited[i] = True # 방문했다고 체크
                q.append([i,c+1])

n, m, k, start = map(int, input().split())
# 1. 맵 생성
arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# 2.길 연결
for i in range(m):
    a, b = map(int, input().split()) # a-b
    arr[a].append(b) # 길 연결
# print(arr)
res = []
bfs(res, start, visited)
# print(res)
# 출력
res = sorted(res)

if len(res)==0: # 도시 없으면 -1
    print(-1)
else:
    for i in res: # 도시 있으면 오름차순으로 출력
        print(i)


