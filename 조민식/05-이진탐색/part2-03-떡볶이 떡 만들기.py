'''
날짜: 2022.09.09
시간복잡도:

문제:
풀이:
15:23 ~ 16:13 (50분)
N = 1,000,000 -> O(N) 안으로?

자르고 남은 떡 줌. 떡길이 제일 짧은애 ~ 제일 긴애로 하나씩 짤라봐서 비교해야한다.
하나씩 다 보면 N^2.

O(logN) 중간길이로 모든배열 빼가면서 하나씩 찾아가면됨.
    -> 정렬된 배열이 아니니까 index로 접근하는건 안됨.

시작점이 min(arr)가 아닌이유
떡이 19라고 1개만 들어오면
0~19사이에 잘라야하는데
19~19로 잘르므로 답이 안나옴

테스트 값
4 6
19 15 10 17
'''

import sys
input = sys.stdin.readline

def binary_search(arr, target, start, end):
    if start > end:
        return None
    res = 1e9 # 남은 떡 길이

    # 떡의 길이로 이진 탐색 할 것이다. 중앙값으로 계속 짜름.
    while True:
        if start > end:
            break
        mid = (start + end) // 2 # 중앙값 10, 19 니까 29//2 => 14로 자름
        temp = 0 # mid로 모든 떡 잘랐을 때 남은 떡 길이
        
        for i in arr: # 떡의 길이 >= 자를길이. 
            if i >= mid: 
                temp += i - mid
        # print(f'start:{start}, end:{end}, mid:{mid}, res:{res}, temp:{temp}') # 0 4 2

        # 목표값보다 많이 남았으므로, 더 길게 잘라서 남은 떡의 길이가 짧게 해야함
        if temp >= target:
            start = mid + 1
            res = mid # 자르면 자를수록 target보다 크고 작은 값으로 수렴함.
        # 목표값보다 작게 남았으므로, 더 짧게 잘라서 남은 떡이 많게 해야함
        else:
            end = mid - 1
    return res

n, m  = map(int, input().split())
arr = list(map(int, input().split()))

print(binary_search(arr, m, 0, max(arr)))
'''

'''

