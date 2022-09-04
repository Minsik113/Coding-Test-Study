# p.360 안테나

n = int(input())
loc = list(map(int, input().split()))

# loc를 오름차순으로 정렬
loc.sort()

total = 0
distance = []
for i in range(loc[-1]+1):
    if i == 0:
        continue
    else:
        for j in loc:
            total += abs(j-i)
        distance.append((i, total))
        total = 0

distance = sorted(distance, key=lambda k: k[1])
print(distance[0][0])

# 답지를 보니 간단하게 중간값을 출력하면 최소값을 구할 수 있다고 함..
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
# print(data[(n-1)/2]