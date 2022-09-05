'''
시간복잡도: O(N + K) 
공간복잡도: O(N + K)
특정한 조건이 부합할 때만 사용가능. 매우빠름
데이터개수(N), 최대양수값(K)

1.K+1개 dictionary만든다.
2.하나씩 개수에 추가
3.각각의 인덱스를 개수만큼 출력
'''
arr = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0]*(max(arr)+1)

# 2. 개수추가
for i in range(len(arr)):
    count[arr[i]] += 1 

for i in range(len(count)): # N + K 임
    for j in range(count[i]): 
        print(i, end=' ')
