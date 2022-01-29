"""
문제 : 거스름돈 동전 갯수
"""

def changes(money:int) -> int:
    coins = [500, 100, 50, 10]
    count = 0
    for coin in coins:
        s, r = divmod(money, coin)
        count += s
        money = r
    return count

print(changes(1160))

