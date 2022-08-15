'''
날짜: 2022.08.16
시간복잡도: # O(NlogN)

문제:
풀이: 최소힙 알고리즘 이용 (정렬로해도됨)
print(ord('A'), ord('Z')) # 65 90
print(s.isalpha()) # True

'''
import heapq

s = input()

list_str = []
sum_int = 0

for i in range(len(s)): # O(nlogn)
    if s[i].isalpha():
        heapq.heappush(list_str, s[i])
    else:
        sum_int += int(s[i])

while list_str: #O(logN)
    print(heapq.heappop(list_str),end='')
print(sum_int)