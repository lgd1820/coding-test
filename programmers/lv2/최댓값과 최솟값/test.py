def solution(s):
    answer = [int(c) for c in s.split()]
    return f"{min(answer)} {max(answer)}"

print(solution("-1 -2 -3 -4"))