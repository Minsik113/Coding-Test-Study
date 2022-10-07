'''
1.기존 다익스트라랑 차이점
- 현재 가장 가까운 노드를 저장해 놓기 위해서 힙 자료구조를 추가적으로 이용한다.
- 현재의 최단 거리가 가장 짧은 노드를 선택해야 하므로 최소 힙을 사용한다.

O(V^2) -> O(ElogV)
'''
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
# 노드 연결 정보
graph = [[] for _ in range(n+1)]
# 최단 거리 테이블
distance = [INF] * (n+1)

# 1. 간선 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있다면 -> 무시
        if distance[now] < dist: # 더 작은 거리로 설정되어있으니 볼 필요 없다.
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])
