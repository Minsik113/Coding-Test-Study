'''
날짜: 2022. 08. 10
시간복잡도: O(N)

문제:
풀이: A가고르면 B가 고를 수 있는 경우만 생각하면서 줄임
'''
n, m = map(int, input().split())
data = list(map(int, input().split()))

check = [0] * (m+1) # 최대무게까지 카운팅할 수 있게 dictionary만들어놓음
for i in data:
    check[i] += 1 # 고른 무게의 볼링공이 몇개인지 카운팅

result = 0
for i in range(1, m+1): # 무게0인건없으니 1~m까지
    n -= check[i] # 전체무게에서 ikg의 개수를 뺸다.
    result += check[i] * n # B가 고를 수 있는 볼링공 개수
print(result)

'''
즉 볼링공무게가 [1,2,3,3,3,2]라면, 총개수6개
1kg = 1개  -> check[1] = 1 1a
2kg = 2개  -> check[2] = 2 2a,2b
3kg = 3개  -> check[3] = 3 3a,3b,3c

유림, 혜영
유림이 1kg짜리고르면
혜영이가 고를 수 있는 볼링공들은 - 1kg을 제외한 모든 볼링공이다.

1. 유림이가 ikg 볼링공을 고르면 혜영이가 고를 수 있는건 전체(n) - ikg무게볼링공(check[i])이다.
2. 전체 무게 = 전체무게 - ikg의 볼링공개수 
3. 혜영이가 고를 수 있는 볼링공 = 지금까지의 골랐던 볼링공 + ()

'''


