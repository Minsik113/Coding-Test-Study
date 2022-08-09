'''
날짜: 2022. 08. 09
시간복잡도:     O(N^2)까지가능

문제:
풀이:
모든경우 다따지면 nCn, N=1000이고 O(N!)라 안됨.
'''
n = input()
coins = list(map(int, input().split()))

# 다 만들어놓고 하나씩 보면 경우의 수 증가하면 틀림
# 하나씩 봐야함. sort
# sort_coins = sorted(coins)
# cost = 0

# for coin in sort_coins:
#     if cost + 1 < coin:
#         break

