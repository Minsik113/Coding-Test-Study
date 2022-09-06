'''
날짜: 2022. 09. 06
시간복잡도: O(NlogN)

문제: https://www.acmicpc.net/problem/10825
풀이: 문제대로 sort 조건 주면 됨

'''

import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    name, kor, en, m = input().split()
    arr.append([name, int(kor), int(en), int(m)])

sort_arr = sorted(arr, key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in range(n):
    print(sort_arr[i][0])
