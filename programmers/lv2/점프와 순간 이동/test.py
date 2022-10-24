def solution(n):
    ans = 1

    while n > 2:
        if n % 2 == 1:
            ans += 1
        n //= 2
    return ans

print(solution(5))
print(solution(6))
print(solution(5000))