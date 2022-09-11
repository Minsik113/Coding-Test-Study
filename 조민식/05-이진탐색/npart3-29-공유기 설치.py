'''
날짜: 2022. 09. 11
시간복잡도:

문제: https://www.acmicpc.net/problem/2110
풀이:
17:39 ~ 

N: 20만, 집위치10억
공유기는 집에 설치. 제일 먼 곳에 설치하면 됨. 최소거리를 바꿔가면서
1. 시작위치에 공유기 하나 박음
2. 최소거리 거리가 1인 위치에 공유기 설치
3. 최소거리 거리가 2인 위치에 공유기 설치 
-> 이대로 가면 N개의 집(O(N))을 M의 거리(O(M))로 O(NM)로 시간초과

설치할 거리를 이진탐색활용

1. 제일 먼 집의 위치를 잡음(입력받을 때 찾을꺼라 O(N))
2. (1 + 제일 먼 거리(최대값)) // 2 의 거리마다 공유기 설치
  2-1. 집이 있으면 거기에 설치
  2-2. 집이 없으면, mid뒤의 집을 찾아봄. (많이 멀면 M만큼 셀텐데?)



테스트 값
5 3
1
2
8
4
9
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)] # O(N)
arr.sort() #O(NlogN) 20만x18정도 -> 400만

def binary_search(arr, m, start):
    res = 0 # mid거리마다 공유기 설치해서 몇개가 나오느냐
    # 예외 처리. 2개 설치할 때
    if m == 2:
        return arr[-1]-arr[0]
    
    end = max(arr) # 시작점, 맨뒤점 
    while (start <= end):
        cnt = 1 # 공유기 개수. 시작 위치에 하나 무조건 세움
        mid = (start + end) // 2
        temp = 0 # 임시로 집들 간 거리를 더할 변수

        # 1. 다음 집까지 거리랑 mid(공유기 간격)비교
        prev = arr[0]
        for i in range(1, n):
            now = arr[i]
            x = now - prev # 이웃한 집들간 차이
            prev = now

            if temp > 0 and temp >= mid: 
                cnt += 1
                temp = 0
            # 1-1. 다음 집까지 거리 > 설치할 수 있는 공유기 간격 -> 설치.
            elif x >= mid:
                cnt += 1
                temp = 0
            # 1-2. 다음 집까지 거리 < 설치할 수 있는 공유기 간격 
            #       -> 그 다음 집까지의 거리도 더해야함
            elif x < mid:
                temp += now
                # 1-2-1. 거리 누적된거로 보자
                if temp >= mid: 
                    cnt += 1
                    temp = 0

        # print(start, end, mid, cnt)

        # 2. 설치개수 비교
        if cnt == m:
            res = mid # m개 설치할때 최대 거리
            start = mid+1 # 
        elif cnt > m: # 생각보다 더 많이 설치했으면 거리를 늘려서 설치해보자.
            start = mid + 1
        else: # 생각보다 너무 조금 설치했으면 거리를 줄여서 설치해보자
            end = mid - 1

    return res

print(binary_search(arr, m, 1))