def solution(n):
    answer = [[0 for j in range(0, i)]for i in range(1, n + 1)]
    x = -1
    y = 0
    num = 1
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1

            answer[x][y] = num
            num += 1

    return sum(answer, [])

print(solution(4))
print(solution(5))
print(solution(6))