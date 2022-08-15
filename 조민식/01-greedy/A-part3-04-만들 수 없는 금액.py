'''
날짜: 2022. 08. 09
시간복잡도:     O(N^2)까지가능

문제:
풀이:
[1,2,3,8]
target      coin        다음타겟(target+coin)       target+coin-1까지 만들 수 있다는말임
1           1           1+1 = 2                     2-1=1이니 1까지 만들 수 있음
2           1,2         2+2 = 4                     4-1=3이니 3까지 만들 수 있음
3
4           1,2,3       4+3 = 7                     7-1=6이니 6까지 만들 수 있음
5
6
7           8   6까지 만들 수 있는데 새로들어오는게 8이라 못만듦 . -> 답 7
'''
n = int(input())
coins = list(map(int,input().split()))
coins.sort()

target = 1
for coin in coins:
    if target >= coin: # 만들 수 있음
        target += coin
    else:
        break
print(target)