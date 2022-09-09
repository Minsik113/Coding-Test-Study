'''
a = [6,7,3,4,-1,-4,-3,0,0,1,2,3,3,3,3,3,3,3,4,4,8,9]
a.sort()
이렇게 정렬 안된배열에서 개수를 찾는거는 그냥 세는게 더빠를듯 O(N)이니까

'''
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value) # left_value가 a배열에 들어 갈 수 있는 가장 작은 idx
    right_index = bisect_right(a, right_value) # right_value가 a배열에 들어 갈 수 있는 가장 큰 idx
    return right_index - left_index

a = [1,2,3,3,3,3,3,3,3,4,4,8,9] # idx=2부터 3시작, idx=9부터 다른수

print(count_by_range(a, 3, 3)) # 값이 3인 데이터 개수 출력
print(count_by_range(a,-1,5)) # 값이 -1 ~ 5인 데이터 개수 출력