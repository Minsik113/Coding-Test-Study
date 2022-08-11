#1 모험가 길드
from collections import deque
n = int(input())
fear = sorted(map(int, input().split()), reverse=True)
groups = 0
fear = deque(fear)

while len(fear)>0:
    groups += 1
    for _ in range(fear[0]):
        fear.popleft()




print(groups)