def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        a = i // n
        b = i % n

        if a < b:
            answer.append(b + 1)
        else:
            answer.append(a + 1)
    return answer


print(solution(3, 2, 5))
print(solution(4, 7, 14))