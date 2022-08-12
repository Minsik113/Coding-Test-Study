# 6. 무지의 먹방라이브
from collections import deque

def solution(food_times, k):
    food_len = len(food_times)

    q = deque()
    for i, j in enumerate(food_times):
        if j != 0:
            q.append(i)
    for _ in range(k):
        if not q:
            break
        idx = q.popleft()
        food_times[idx] -= 1
        if food_times[idx] != 0:
            q.append(idx)
    answer = -1 if not q else q.popleft()+1
    return answer