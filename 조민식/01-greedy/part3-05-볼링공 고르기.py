'''
날짜:
시간복잡도: O(N^2) n=1000이라가능. 더짧게는?
문제:
풀이: n
'''
import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
bolls = list(map(int,sys.stdin.readline().split()))

cnt = 0
for a, b in combinations(bolls, 2): 
    if a != b:
        cnt += 1
print(cnt)
