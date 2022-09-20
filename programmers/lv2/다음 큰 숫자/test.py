def solution(n):
    answer = n
    while True:
        answer += 1
        if bin(n)[2:].count("1") == bin(answer)[2:].count("1"):
            break

    return answer

print(solution(78))