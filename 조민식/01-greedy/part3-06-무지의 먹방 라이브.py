# '''
# 실패함.
# '''
# from collections import deque
# def solution(food_times, k):
#     answer = 0
#     queue = []
#     total_len = len(food_times)
#     dict_idx = dict() # idx=0, idx=1 저장
    
#     for i in range(total_len): # O(N)
#         queue.append((food_times[i],i+1))
#         dict_idx[i+1] = 0
        
#     q = deque(sorted(queue, key=lambda x: x[0])) # O(NlogN)
#     # print(q)
    
#     prev = 0 # 직전의 최소 걸렸던 시간
#     save_time = 0 # 현재까지의 시간 기록
#     flag = False
#     while q: # O(nlogn)
#         t, idx = q.popleft() # 먹는데 걸리는 시간, index
        
#         # 3-1.가장 작은시간 걸리는 음식 뽑아야함. 예시가 k초까지 먹는거라서 =붙임
#         if k >= ((t-prev) * total_len + save_time): 
#             save_time += (t-prev) * total_len
#             prev = t
#             total_len -= 1
#             dict_idx[idx] = 1 # 얘는 끝남.
#         # 3-2. 지금까지 먹은 시간사이에 장애발생. 이안에 정답이 나오는 경우임 
#         else: 
#             q.append((t,idx))
#             flag = True
#             break
    
#     # 더 섭취할 음식이 없을 경우
#     if not flag:
#         return -1
#     # 남은 queue 다꺼내서 -> k번째가 답.
#     cnt = 0
#     for i in range(total_len):
#         if cnt == k-save_time:
#             answer = i+1
#             break
#         if dict_idx[i+1] != 1:
#             cnt += 1
        
    
#     return answer