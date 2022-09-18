'''
An = A(n-1) + A(n-2) , 단, a1=x, a2=y

재귀 -> O(2^N) 
하나의 값을 구하려면 아래2개의 값을 구해야하니까 2배씩 늘어남.
같은곳을 또 들른다. 불필요한 부분을 또 봄.

fibo(30)을 계산하기 위해 약 10억 가량의 연산을 수행해야함.

'''
# 재귀
def fibo(x):
    if x==1 or x==2:
        return 1
    return fibo(x-1) + fibo(x-2)
print(fibo(4))