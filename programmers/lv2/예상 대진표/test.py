import math

def solution(n,a,b):
    answer = 0

    min_num = min(a, b)
    max_num = max(a, b)
    while min_num != max_num:
        min_num = math.ceil(min_num / 2)
        max_num = math.ceil(max_num / 2)
        answer += 1

    return answer

print(solution(8, 4, 7))