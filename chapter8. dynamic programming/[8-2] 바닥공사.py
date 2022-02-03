dp = [0] * 1001
dp[1], dp[2] = 1, 3

def floor():
    n = int(input())
    for n in range(3, n+1):
        dp[n] = ( dp[n-1] + 2* dp[n-2] ) % 796796                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    return dp[n]

print(floor())

# 3 -> 5
# 4 -> 11
