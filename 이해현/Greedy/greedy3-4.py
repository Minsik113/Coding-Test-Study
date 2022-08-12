#4. 만들수 없는 금액
import numpy as np
n = int(input())
coin = list(map(int, input().split()))

coin.sort()
result = 1

for c in coin:
    if result < c:
        break

    result+=c

print(result)