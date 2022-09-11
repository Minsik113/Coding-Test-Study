import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
# N = 5
# arr = [-15, -6, 1, 3, 7]


def binary_search(array, start, end):
    if start > end:
        return print(-1)
    mid = (start + end) // 2
    if array[mid] == mid:
        return print(mid)
    elif array[mid] > mid:
        binary_search(array, start, mid - 1)
    else:
        binary_search(array, mid + 1, end)


binary_search(arr, 0, N - 1)

