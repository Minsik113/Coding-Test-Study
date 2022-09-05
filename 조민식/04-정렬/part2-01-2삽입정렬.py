'''
시간복잡도: O(N^2)
공간복잡도: O(N)
매번 왼쪽에 있는 데이터크기를 비교함.
위치를 이동한다.
'''
arr = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(arr)): # 2번째 원소부터보면됨. 1번은 정렬되어있는거임
    for j in range(i, 0, -1): # i부터 1까지 -1한다.
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else: 
            break
print(arr)