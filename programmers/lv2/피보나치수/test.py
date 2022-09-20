def solution(n):
    if n <= 2:
        return 1
    
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b
    
    return b % 1234567

print(solution(3))
print(solution(5))