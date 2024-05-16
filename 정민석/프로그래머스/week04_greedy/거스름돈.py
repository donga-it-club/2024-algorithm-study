n = int(input())
count = 0

n = 1000 - n

coin_types = [500, 100, 50, 10, 5, 1]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)
