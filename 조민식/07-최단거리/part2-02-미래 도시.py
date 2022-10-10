'''
날짜: 2022.10.10
시간복잡도: O(N^3)

문제:
풀이:
23:50 ~ 00:02

양방향 이동 가능
간선마다 거리 => 1
한지점에서 한 지점까지의 최단거리 -> 다익스트라, 플로이드워셜
n이 100까지니까 플로이드워셜 가능

테스트 케이스1
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
테스트 케이스2
4 2
1 3
2 4
3 4
'''
import sys
input = sys.stdin.readline

# 0. 최단거리 세팅
n, m = map(int, input().split())
INF = 1e9
graph = [[INF] * (n+1) for _ in range(n+1)]
for a in range(1, n+1): # 자기자신으로 가는 길은 0
    graph[a][a] = 0

# 1. 간선 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

end, passstop = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
print(graph)

k = graph[1][passstop] + graph[passstop][end]
if k >= INF:
    print(-1)
else:
    print(graph[1][passstop] + graph[passstop][end])

