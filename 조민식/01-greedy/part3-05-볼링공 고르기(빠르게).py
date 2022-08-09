'''
날짜: 2022. 08. 10
시간복잡도: O(N)

문제:
풀이: A가고르면 B가 고를 수 있는 경우만 생각하면서 줄임
'''
n, m = map(int, input().split())
data = list(map(int, input().split()))

check = [0] * (m+1) # m최대무게
for i in data:
    check[i] += 1

result = 0
for i in range(1, m+1): # 무게0인건없으니 1~m까지
    n -= check[i] # A가 i무게를 고르면
    result += check[i] * n # B가 고를 수 있는 볼링공 개수
print(result)