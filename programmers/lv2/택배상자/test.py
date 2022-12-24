def solution(order):
    answer = []
    sub = []
    for i in range(len(order)):
        if sub:
            while sub[-1] == order[len(answer)]:
                answer.append(sub.pop())
                if not sub:
                    break

        if i + 1 == order[len(answer)]:
            answer.append(i + 1)
        else:
            sub.append(i + 1)

    
    if sub:
        while sub[-1] == order[len(answer)]:
            answer.append(sub.pop())
            if not sub:
                break

    return len(answer)

print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))