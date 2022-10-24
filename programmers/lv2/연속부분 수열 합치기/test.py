def solution(elements):
    answer = []
    temp = elements * 2

    for i in range(1, len(elements) + 1):
        answer += [sum(temp[j:j+i]) for j in range(len(temp) - i)]
    return len(set(answer))

print(solution([7,9,1,1,4]))