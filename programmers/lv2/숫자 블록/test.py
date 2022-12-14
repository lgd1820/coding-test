import math

def solution(begin, end):
    answer = []

    for i in range(begin, end + 1):
        if i == 1:
            answer.append(0)
        else:
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    mok = i // j
                    if mok > 10 ** 7:
                        continue
                    answer.append(i // j)
                    break
            else:
                answer.append(1)
    return answer

print(solution(1, 10))