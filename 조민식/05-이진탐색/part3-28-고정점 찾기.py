'''
날짜:  2022.09.11
시간복잡도: O(logN)

문제:
서로 다름, 오름차순 정렬.
고정점있으면 출력(최대1개), 없으면 -1출력

풀이:
17:28~ 17:38

인덱스에 해당하는 arr값이 더 크면 왼쪽으로
즉, idx < arr[idx] -> 더 왼쪽을 보자
idx > arr[idx] -> 오른쪽을 보자
발견하면 idx, 없으면 -1 출력

테스트 값
5
-15 -6 1 3 7

7
-15 -4 3 8 9 13 15
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def search_binary(arr, start, end):
    
    while start <= end:
        mid = (start + end) // 2 # index = mid
        # 정답 출력
        if mid == arr[mid]:
            return mid
        elif mid < arr[mid]: # 더 왼쪽으로
            end = mid -1
        else:
            start = mid + 1
    return -1

print(search_binary(arr, 0, n-1))

