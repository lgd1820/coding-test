def solution(n):
    dp = [0, 3, 11]
    index = n // 2
    if n % 2 != 0:
        return 0
    
    for i in range(3, index + 1):
        dp.append((3 * dp[i-1] + sum(dp[1:i-1]) * 2 + 2) % 1000000007)
    return dp[-1]

print(solution(4))