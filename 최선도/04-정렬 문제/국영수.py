# 백준 10825 python3 시간초과 / pypy3 통과
# 그냥 input으로 하면 시간초과
import sys

n = int(sys.stdin.readline())

rating = []

for _ in range(n):
    name, kor, eng, math = sys.stdin.readline().split()
    rating.append([name, int(kor), int(eng), int(math)])
    
rating = sorted(rating, key=lambda x : (-x[1], x[2], -x[3], x[0]))

for x in rating:
    print(x[0])