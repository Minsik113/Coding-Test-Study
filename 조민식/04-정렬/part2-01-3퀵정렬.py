'''
시간복잡도: O(NlogN) 
공간복잡도: O(N)
N개의 데이터를 이등분하여 낱개가 될때까지 정렬하는 알고리즘
N x logN(N을 계속 2등분하니까) = NlogN
최악은O(N^2) => 이미 정렬된 배열의 경우, pivot보다 작고 큰애가 안생겨서 오른쪽만 남게된다. 
N x n-1 x ... 1 이 되므로 N^2이됨.
'''

arr = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(arr, start, end):
    if start >= end: # 한 사이클 다 보면 리턴
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end

    while (left <= right):
        # left -> pivot보다 크거나 값은값 나올 때 까지
        while (left <= end and arr[left] <= arr[pivot]):
            left += 1
        # right -> pivot보다 작거나 같은값 나올 때 까지
        while (right > start and arr[right] >= arr[pivot]):
            right -= 1
        # 엇갈렸다면 작은 데이터와 피벗을 교체 (한 사이클 끝)
        if (left > right):
            arr[right], arr[pivot] = arr[pivot], arr[right]
        # 엇갈린게 아니라면 left랑 right위치 교체
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    quick_sort(arr, start, right-1) # 왼쪽 덩어리
    quick_sort(arr, right+1, end) # 오른쪽 덩어리

quick_sort(arr, 0, len(arr)-1)
print(arr)