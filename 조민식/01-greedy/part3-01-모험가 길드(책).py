import math
import time

import random
a = []
for _ in range(2000000):
    a.append(random.randint(1, 100))  # 1부터 100 사이의 임의의 정수

start = time.time()
# n = int(input())
# a = list(map(int, input().split()))
a.sort() # O(NlogN)

ans = 0
count = 0

for i in a: # O(N)
    count += 1
    if count >= i:
        ans += 1
        count = 0

print(ans)

end = time.time()
print(f"{end - start:.5f} sec")