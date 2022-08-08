price = int(input())
cnt = 0

coin_type = [500, 100, 50, 10]

for coin in coin_type:
    cnt += price // coin
    price = price % coin
    
print(cnt)
