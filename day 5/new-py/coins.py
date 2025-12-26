Find minimum number of coins.py

def min_coins(V):
    coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    ans = []

    for i in range(len(coins) - 1, -1, -1):
        while V >= coins[i]:
            V -= coins[i]
            ans.append(coins[i])

    return ans


V = 49
ans = min_coins(V)

print(len(ans))
print(*ans)
