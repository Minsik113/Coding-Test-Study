'''
날짜: 2022.08.08
시간복잡도: O(NlogN). O(NlogN)까지가능

문제: 최대 팀수
풀이: 우선순위큐로 저장할까? 

sort보다는 빨라보임
'''
import math
import time
import heapq

import random
numbers = []
for _ in range(2000000):
    numbers.append(random.randint(1, 100))  # 1부터 100 사이의 임의의 정수

start = time.time()
# n = int(input()) 
# numbers = list(map(int, input().split()))
ans = 0 # 팀 수

dict_number = dict()
for i in numbers: # O(N)
    if i in dict_number:
        dict_number[i] += 1
    else:
        dict_number[i] = 1
# print(dict_number)

heap = []
for k,v in dict_number.items(): # O(logN)
    heapq.heappush(heap,(k,v))

temp = 0
while heap: # O(NlogN)
    k, num = heapq.heappop(heap) # k가 num개있다. 
    if k <= num: # 팀으로 만들 수 있으니 개수 더해주자
        ans += num // k # 개수 더해줌
        temp += num % k # 남은거 
    else: # 팀으로 만들 수 없으니 남아있는 사람이랑 비교
        save = (temp + num)
        if k <= save: # 남아있는사람들과합쳤을때 팀이 꾸려진다면
            ans += save // k # 만들 수 있는 팀만큼 추가하고
            temp = save - (save // k) # 남은수 저장
        else: # 팀못꾸렸다면 temp에 추가
            temp += num
print(ans)
end = time.time()
print(f"{end - start:.5f} sec")

