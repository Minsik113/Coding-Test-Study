'''
날짜: 2022.10.29
시간복잡도:

문제:
https://www.acmicpc.net/problem/12865
풀이:
그리디. N=100임. O(N^3)까지 가능.
무게를 넘지않고 최대의 가치

물건을 배낭에 담을 때,
1.현재 배낭의 허용 무게보다 넣을 물건의 무게가 더 크다면 넣지 않는다
2.그렇지 않다면 아래중 더 나은애를 고른다
2-1.현재 넣을 물건의 무게만큼 배낭에서 뺀다. 그리고 현재 물건을 넣는다.
2-2.현재 물건을 넣지 않고 이전 배낭 그대로 가지고 간다.
'''
n, k = map(int,input().split())

arr = [[0,0]]
# 넣어줌
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 그리드시작
d = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1): # 배낭 봐야지
    for j in range(1, k+1): # 가능한 무게
        w = arr[i][0]
        v = arr[i][1]

        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j-w]+v, d[i-1][j])
print(d)