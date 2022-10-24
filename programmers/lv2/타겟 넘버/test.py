def solution(numbers, target):
    
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))