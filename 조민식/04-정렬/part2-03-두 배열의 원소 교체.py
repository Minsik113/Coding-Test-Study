'''
날짜: 2022. 09. 06
시간복잡도:

문제:
풀이:
N=10만 -> O(NlogN)까지가능

A리스트 B리스트 받는다.
A와 B리스트을 최대 K번 바꿔서 A리스트의 합을 최대로 만들자.

테스트값
5 3
1 2 5 4 3
5 5 6 6 5
'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a = sorted(a) 이러면 메모리 낭비남
# b = sorted(b, reverse=True)
a.sort() 
b.sort(reverse=True)

idx_a = 0
idx_b = 0
while True:
    # 종료조건1. 모든 기회 다 씀
    if k <= 0:
        break

    if a[idx_a] < b[idx_b]:
        a[idx_a],b[idx_b] = b[idx_b],a[idx_a] # 바꿈
        idx_a += 1 # 위치이동
        idx_b += 1
        k -= 1
    else: # 종료조건2. 바꿀게 없으면 종료해야지
        break

print(a)
print(sum(a))