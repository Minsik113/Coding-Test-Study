'''
날짜:  2022. 08. 16
시간복잡도: 3중for문있는곳인데 얼마나걸리는거지?

문제:
풀이:
(r,c)
0,0 0,1 0,2
1,0 1,1 1,2
2,0 2,1 2,2
'''
# 빈칸(0) 집(1) 치킨집(2)
import sys
from itertools import combinations
n, m = map(int, input().split())

arr = [] # 맵
pos_home = [] # 집좌표
pos_fried = [] # 치킨좌표 
for i in range(n): # O(N^2)
    temp = list(map(int, input().split()))
    arr.append(temp)
    for j in range(n):
        if temp[j] == 1:
            pos_home.append((j, i)) # 집위치
        elif temp[j] == 2:
            pos_fried.append((j, i))

# print(pos_fried)
# print(pos_home)

# 치킨집에서 집까지의 거리 구하자
ans = sys.maxsize
# 1. m개의 치킨집뽑음
for choosed in combinations(pos_fried, m): 
    # 2. 모든 집에 대해서 m개의 치킨집의 최소거리를 구해야함.
    # print(f'골라진 집 {choosed}') 
    sum_save = 0
    for hx, hy in pos_home: # 모든 집
        temp = sys.maxsize # m개의 치킨집이 뽑혔을때, 집까지 거리중 제일 가까울 때 거리 저장하려는 변수
        for fx, fy in choosed: # 치킨집 거리
            temp = min(temp, abs(fx-hx)+abs(fy-hy)) # 최솟값만 찾아라
        # 2-1.(hx,hy)에 위치한 집은 temp라는 치킨거리를 갖는다.
        sum_save += temp 
    # 선택된 치킨집에 한하여, 모든집에서 선택된 치킨집 사이의 거리는 sum_save이다.

    ans = min(ans, sum_save)
    # print(sum_save, ans)
print(f'{ans}')