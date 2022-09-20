def solution(numbers):
    answer = 0
    numbers = sorted(list(set(numbers)))
    for i in range(10):
        if i not in numbers:
            answer+= i
    return answer

print(solution([1,2,3,4,6,7,8,0]))

