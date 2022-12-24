def solution(target):    
    score_list = [[i for i in range(1, 21)] + [50], [i*2 for i in range(1, 21) if i*2 > 20] +  [i*3 for i in range(1, 21) if i*3 > 20]]
    
    dp = [[100000, 0] for _ in range(target + 1)]
    dp[0][0] = 0

    for i in range(1, target+1):
        for j in range(2):
            for k in range(len(score_list[j])):
                prev = i - score_list[j][k]

                if prev < 0:
                    continue
            
                total, valid = dp[prev][0] + 1, dp[prev][1] + 1 - j

                if total < dp[i][0]:
                    dp[i] = [total, valid]
                elif total == dp[i][0]:
                    dp[i] = [total, max(dp[i][1], valid)]

    return dp[target]

print(solution(21))
print(solution(58))