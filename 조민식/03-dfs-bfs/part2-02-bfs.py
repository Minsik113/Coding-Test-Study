from collections import deque

def bfs(graph, start, visited):
    # 덱 사용
    q = deque([start])
    # 현재 노드 방문처리
    visited[start] = True
    # 큐가 없을 때까지 반복
    while q:
        v = q.popleft()
        print(v,end=' ')
        # 아직 방문안한 인접노드 삽입
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True



graph = [
    []
    ,[2,3,8]
    ,[1,7]
    ,[1,4,5]
    ,[3,5]
    ,[3,4]
    ,[7]
    ,[2,6,8]
    ,[1,7]
]
visited = [False] * 9
bfs(graph, 1, visited)