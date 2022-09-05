# 집의 위치를 정렬 후 가운데에 가장 가까운 수를 찾아내면 되지 않을까
# 입력이 20만개 이상 들어올 경우를 생각해 sys.stdin.readline() 사용

import sys

N = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))

line.sort()
print(line[(N - 1) // 2])  # 인덱스는 0부터기 때문에 N을 그대로 넣으면 우측으로 쏠림
