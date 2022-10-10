INF = int(1e9)

n = int(input())
m = int(input())

# 1. 도시간의 거리를 저장할 2차 배열 선언
graph = [[INF] * (n+1) for _ in range(n+1)]
for a in range(1, n+1): # 자기 자신으로 가는 비용은 0 으로 초기화
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 2.간선 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c # 방향 그래프

# 3. Floyd-Warshall 알고리즘
for k in range(1, n+1): # 거쳐가는 노드
    for a in range(1, n+1): # 출발 노드
        for b in range(1, n+1): # 도착 노드
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("Infinity", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()

