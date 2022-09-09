'''
날짜: 2022. 09. 09
시간복잡도:

문제:
풀이:

정렬된 배열에서 특정 수들의 개수를 구하는 것임.
 =>bisect_right - bisect_left로 들어가는 개수 구하면 됨

테스트 값
7 2
1 1 2 2 2 2 3
'''

from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

def count_by_range(arr, left_value, right_value):
    start = bisect_left(arr, left_value)
    end = bisect_right(arr, right_value)
    return end - start

n, m = map(int, input().split())
arr = list(map(int, input().split()))
res = count_by_range(arr, m, m)

if res == 0:
    print(-1)
else:
    print(res)
