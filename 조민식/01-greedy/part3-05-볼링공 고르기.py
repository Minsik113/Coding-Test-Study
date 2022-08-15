'''
날짜:
시간복잡도: O(N^2) n=1000이라가능. -> 100만  -> 풀때 200만 언저리로나오게해야하는데 더짧게는?
O(N)

문제:
풀이: n
'''
import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
bolls = list(map(int,sys.stdin.readline().split()))

cnt = 0
for a, b in combinations(bolls, 2):  # 2중 for문 
    if a != b: # 같은 무게 안고름.
        cnt += 1
    print(f'({a},{b}), ',end=' ')
print(cnt)
