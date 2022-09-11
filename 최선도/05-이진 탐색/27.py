# bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# bisect_right(a, x) : 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
# 시간 복잡도 : O(logN)

import sys
from bisect import bisect_left, bisect_right

N, x = map(int, sys.stdin.readline().split())
list_x = list(map(int, sys.stdin.readline().split()))
# N, x = 7, 2
# list_x = [1, 1, 2, 2, 2, 2, 3]

answer = bisect_right(list_x, x) - bisect_left(list_x, x)
if answer == 0:
    print(-1)
else:
    print(answer)

