'''
날짜: 2022.09.06
시간복잡도: O(nlogn)

문제:
풀이: 그냥 단순 소트

테스트값
2
홍길동 95
이순신 77
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    name, score = input().split()
    arr.append([name, int(score)])

arr = sorted(arr, key=lambda x:x[1])

for i in arr:
    print(i[0], end=' ')

    