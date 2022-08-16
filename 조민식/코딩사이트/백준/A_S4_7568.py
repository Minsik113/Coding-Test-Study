n = int(input())

info_menbers = [list(map(int, input().split())) for _ in range(n)]

result = []
for i in range(n):
    prev = info_menbers[i]
    k = 0  # 자신보다 큰 사람 저장
    for j in range(n):
        now = info_menbers[j]
        if prev[0] < now[0] and prev[1] < now[1]:
            k += 1 # 자신보다 큰 사람의 수 저장
    result.append(k+1)
    
for i in result:
    print(i,end=' ')