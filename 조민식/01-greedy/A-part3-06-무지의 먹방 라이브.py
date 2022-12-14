# 
'''
실패함.

from collections import deque
def solution(food_times, k):
    answer = 0
    queue = []
    total_len = len(food_times)
    dict_idx = dict() # idx=0, idx=1 저장
    
    for i in range(total_len): # O(N)
        queue.append((food_times[i],i+1))
        dict_idx[i+1] = 0
        
    q = deque(sorted(queue, key=lambda x: x[0])) # O(NlogN)
    # print(q)
    
    prev = 0 # 직전의 최소 걸렸던 시간
    save_time = 0 # 현재까지의 시간 기록
    flag = False
    while q: # O(nlogn)
        t, idx = q.popleft() # 먹는데 걸리는 시간, index
        
        # 3-1.가장 작은시간 걸리는 음식 뽑아야함. 예시가 k초까지 먹는거라서 =붙임
        if k >= ((t-prev) * total_len + save_time): 
            save_time += (t-prev) * total_len
            prev = t
            total_len -= 1
            dict_idx[idx] = 1 # 얘는 끝남.
        # 3-2. 지금까지 먹은 시간사이에 장애발생. 이안에 정답이 나오는 경우임 
        else: 
            q.append((t,idx))
            # res = sorted(q[t:],key=lambda x:x[1])
            flag = True
            break
    
    # 더 섭취할 음식이 없을 경우
    if not flag:
        return -1
    # 남은 queue 다꺼내서 -> k번째가 답.
    cnt = 0
    for i in range(total_len):
        if cnt == k-save_time:
            answer = i+1
            break
        if dict_idx[i+1] != 1:
            cnt += 1
        
    
    return answer
'''

# 
# 런타임에러
'''
# -> 런타임 에러남. 속도 . ㅎ  ㅏ 
시간복잡도: O(NlogN)이하까지 가능.

전체개수(n), 제일 작은거(m) 
if k > n*m:
    count += (n*m)
    k -= (n*m)
else:
    k번째+1에 있는애가 답.

heapq에넣고 하나씩 뺴쓸까 뺴는데 O(logN) 
넣는거 O(logN)
import heapq
def solution(food_times, k):
    answer = 0
    heap = []
    total_len = len(food_times) # O(1)
    # 1.heap에 (먹는데걸리는시간, index) 저장
    for i in range(total_len): # O(NlogN)
        heapq.heappush(heap, (food_times[i],i+1)) # 답은 이 index임
    # 2. 제일작은애 pop
    prev = 0 # 직전의 최소 걸렸던 시간
    save_time = 0 # 현재까지의 시간 기록
    
    while heap: # O(NlogN)
        t, idx = heapq.heappop(heap) # 먹는데걸리는시간, index
        
        # 3-1.가장 작은시간 걸리는 음식 뽑아야함. 예시가 k초까지 먹는거라서 =붙임
        if k >= ((t-prev) * total_len + save_time): 
            save_time += (t-prev) * total_len
            prev = t
            total_len -= 1
        # 3-2. 지금까지 먹은 시간사이에 장애발생. 이안에 정답이 나오는 경우임 
        else: 
            heapq.heappush(heap,(t,idx))
            break  
            
    # 남은 heap 다꺼내서 -> idx 정렬 후 -> k번째가 답.
    # print(heap)
    res = []
    while heap:
        res.append(heapq.heappop(heap)[1])
    res.sort()
    answer = res[k-save_time]
    
    return answer
'''