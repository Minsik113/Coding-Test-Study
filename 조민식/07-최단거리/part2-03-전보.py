'''
날짜: 2022.10.11
시간복잡도:

문제:
풀이:
00:31 ~ 

1. C에서 출발하여 갈 수 있는 도시들의 개수는 총 몇개인가
2. C와 제일 먼 거리에 연결된 도시는 거리가 얼마나 걸리는가

bfs로 시간재자.

테스트 케이스
3 2 1
1 2 4
1 3 2
'''
import heapq
from multiprocessing import heap
import sys
input = sys.stdin.readline

# n:도시 개수, m:간선 개수, c:출발 도시
n, m, start = map(int, input().split())
# 노드 연결 정보
graph = [[] for _ in range(n+1)]
# 최단거리 테이블
distance = [1e9] * (n+1)

for _ in range(m):
    # a->b로 이동하는데에 c시간이 걸린다.
    a, b, c = map(int, input().split())
    graph[a].append((b,c)) 

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 이미 더 빠른 길이 있다.
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 도달할 수 있는 도시 수
print(distance)
cnt = 0 
max_distance = 0
for i in range(1, n+1):
    if distance[i] != 1e9:
        cnt += 1
        max_distance = max(max_distance, distance[i])

print(cnt-1, max_distance)