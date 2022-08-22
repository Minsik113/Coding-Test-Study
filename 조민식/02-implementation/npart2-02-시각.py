'''
날짜: 2022. 08. 18
시간복잡도: O(N^3)이지만 24*60*60=86400이면 끝

문제:
풀이:d 아래럼 풀지말고 답지처럼..ㅋ;

시  분  초
x   x   o
x   o   x
o   x   x
x   o   o
o   x   o
o   o   x
o   o   o
1.시에 3들어감)
  1-1.분에3들어감)
    2-1-1.초에들어감    ()*15*15
    2-1-2.초에안들어감  (n+1)*15*60
  1-2.분에3안들어감)
    2-2-1.초에들어감    (n+1)*60*15
    2-2-2.초에안들어감
  
2.시에 3안들어감)
 2-1.분에3들어감)
    2-1-1.초에들어감    (n+1)*15*15
    2-1-2.초에안들어감  (n+1)*15*60
 2-2.분에3안들어감)
    2-2-1.초에들어감    (n+1)*60*15

'''
n = int(input())
ans = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            total_str = str(i) + str(j) + str(k)
            if '3' in total_str:
                ans += 1
print(ans)

# n = int(input())
# ans = 0

# default_count = 1216
# t=0
# if n == 23: # 시간에 3이 3번
#     t = 3
# elif n >= 13: # 시간에 3이 2번
#     t = 2
# elif n >= 3: # 시간에 3이 1번
#     t = 1
# else: # 시간에 3이 0번
#     pass
# ans = default_count * (n+1-t) # 0시도 16*16번 이므로
# ans += 3600 * t

# print(ans)    


