def solution(brown, yellow):
    x_plus_y = (brown + 4) // 2
    
    for i in range(3, x_plus_y):
        print(i, x_plus_y - i)
        if (i - 2) * (x_plus_y - 2 - i) == yellow:
            return [x_plus_y - i, i]

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))