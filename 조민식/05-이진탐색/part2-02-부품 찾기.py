'''
날짜:  2022.09.11
시간복잡도: O(N+M)

문제:
풀이:
16:55 ~ 17:05

1. dict로 선언해두고 있는지 없는지 봐도 될듯? O(N+M)
2. set()에 넣어서 보면될듯 O(N)
3. 이진탐색은 정렬해야하므로 O(NlogN)
    + 탐색(logN)xM개
    = NlogN + MlogN = (N+M)logN

set -> dictionary -> 이진탐색

테스트 값
5
8 3 7 9 2
3
5 7 9
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
find_num = list(map(int,input().split()))

dict_num = dict()
for i in arr:
    if i not in dict_num:
        dict_num[i] = 1

for i in find_num:
    if i in dict_num:
        print("yes", end=' ')
    else:
        print("no",end=' ')


