'''
10 7
1 3 5 7 9 11 13 15 17 19
'''
def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾기 시작
    if arr[mid] == target:
        return mid
    elif arr[mid] > target: # end = mid-1
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)

n, target = map(int, input().split())
arr = list(map(int, input().split()))

res = binary_search(arr, target, 0, n-1) # 배열, 목표값, 시작idx, 끝idx
if res == None:
    print("원소 없음")
else:
    print(f'{res+1}에 위치함')