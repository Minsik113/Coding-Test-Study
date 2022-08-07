total = 1250
ans = 0

coins = [500, 100, 50, 10]

for coin in coins:
    ans += total // coin
    total = total % coin
print(ans)
