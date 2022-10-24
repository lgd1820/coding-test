from itertools import permutations

def is_prime_number(x):
    if x <= 1: return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0 
    numbers = [s for s in numbers]
    p_num = []
    for i in range(1, len(numbers)+1):
        num = [int(''.join(per)) for per in list(permutations(numbers, i))]
        p_num += num
    
    p_num = list(set(p_num))

    for num in p_num:
        if is_prime_number(num):
            answer += 1
    return answer

print(solution("17"))
print(solution("011"))