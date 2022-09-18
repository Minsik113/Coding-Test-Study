'''

'''

# 1. 하향식 -> O(N)
# 메모이제이션을 위한 리스트 초기화
d = [0] * 100

def fibo(x):
    if x==1 or x==2:
        return 1
    # 이미 계산한 적이 있다면 그대로 반환
    if d[x] != 0: 
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식 적용해서 저장해둠
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]
# f(6) f(5) f(4) f(3) f(2) f(1) f(2) f(3) f(4)
print(fibo(6))

# 2. 보텀업 
# 작은문제부터 해결하고, 작은문제 조합해서 앞으로의 큰 문제 해결
d = [0] * 100

d[1] = 1
d[2] = 1
n = 6

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n])