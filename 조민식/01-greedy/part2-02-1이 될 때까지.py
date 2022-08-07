'''
날짜:2022.08.08
시간복잡도:O(logN)

문제:
풀이:나눌 수 있으면 나누고, 안되면 1빼자. 
'''
n, k = map(int, input().split())
ans = 0

while n > 1:
    if n % k == 0: # 나누어 떨어지면
        n //= k
    else:  
        n -= 1
    ans += 1
print(ans)        