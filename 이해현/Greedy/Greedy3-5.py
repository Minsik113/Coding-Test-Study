n, m = map(int, input().split())
w = list(map(int, input().split()))

result = 0

for i in range(0,n):
    for j in range(i+1, n):
        if w[i] != w[j]:
            result +=1

print(result)