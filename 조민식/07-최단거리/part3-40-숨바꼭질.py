'''
날짜: 2022.10.11
시간복잡도: O(ElogV)

문제:
풀이:
16:44 ~ 17:27

양방향 통로
-> 1번에서 나머지 통로로 이동할 수 있는 가장 짧은 거리를 저장

테스트케이스1
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''
import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# n = 20000이라 2차원안됨.
graph = [[] for _ in range(n+1)] 
distance = [1e9] * (n+1) # 1번부터 n번째 도시까지 걸리는 거리

# 1.경로 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b,1)) # a->b까지 거리 1걸림
    graph[b].append((a,1))

# 2. dijkstra
def dijkstra(graph):
    q = []
    heapq.heappush(q, (0, 1)) # 걸리는 거리, 시작노드
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 이미 더 빠른 길이 있음
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]: # i[0]번째 노드를 들르는게 더 빠르다면
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(graph)
# print(distance)
max_value = 0
for i in range(1, n+1):
    if distance[i] < 1e9:
        max_value = max(max_value, distance[i])
target = 0
flag = True
cnt = 0
for i in range(1,n+1):
    if distance[i] == max_value:
        if flag:
            target = i
            flag = False
            cnt += 1
        else:
            cnt += 1
print(target,max_value,cnt)