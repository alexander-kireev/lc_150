from math import inf

def c(coins, amount):
    dp = [inf] * (amount + 1)
    dp[0] = 0

    for a in range(amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], dp[a - c] + 1)

    return dp[amount] if dp[amount] != inf else -1

coins = [1,2,5]
amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
print(c(coins, amount))