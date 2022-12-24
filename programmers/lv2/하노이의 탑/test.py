answer = []
def hanoi(N, start, to, via):
    if N == 1:
        answer.append([start, to])
        print(1, start, to)
    else:
        hanoi(N-1, start, via, to)
        answer.append([start, to])
        hanoi(N-1, via, to, start)

def solution(n):
    hanoi(n, 1, 3, 2)
    return answer

print(solution(2))