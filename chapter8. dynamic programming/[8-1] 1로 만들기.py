dp = [0] * 30
def make_one(n):
    for i in range(2, n+1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if i % 5 == 0:
          dp[i] = min(dp[i], dp[i // 5] + 1)
    return dp[n]

print(make_one(26))
print(dp)
print(dp[9])
