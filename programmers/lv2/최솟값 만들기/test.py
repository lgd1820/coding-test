def solution(A,B):
    if len(A) < len(B):
        B = sorted(B, reverse=True)
        answer = sum([a * B.pop(0) for a in sorted(A)])
    else:
        A = sorted(A, reverse=True)
        answer = sum([b * A.pop(0) for b in sorted(B)])
    return answer

# 1 4 2, 5 4 4
# 5 8 16

# 1 2, 3 4
# 