import math
import time

import random
# a = []
# for _ in range(2000000):
#     a.append(random.randint(1, 100))  # 1부터 100 사이의 임의의 정수

# start = time.time()
n = int(input())
a = list(map(int, input().split())) 
a.sort() # O(NlogN)

ans = 0 # 완성된 팀 개수
count = 0 # 팀원모집중인 팀

for i in a: # O(N)  [1,2,2,2,3]
    count += 1 # 팀원 수 1명증가 -> 1 
    if count == i: # 현재팀원수(새로들어온 사람까지)가 방금들어온사람의 번호랑 같거나 크면 팀생성
        ans += 1 # 조 1개 탄생 
        count = 0 # 팀원 초기화

print(ans)

# end = time.time()
# print(f"{end - start:.5f} sec")