from itertools import combinations_with_replacement

def solution(n, info):
    cwr = combinations_with_replacement([i for i in range(11)], n)

    max_r_score = [-1] * 12
    for com in cwr:
        cur = [0] * 12
        for c in com:
            cur[10-c] += 1
        
        
        for i in range(0, 11):
            if info[i] < cur[i]:
                cur[-1] += 10 - i   
            elif info[i] != 0:
                cur[-1] -= 10 - i

        
        if cur[-1] <= 0:
            continue
        
        if cur[::-1] > max_r_score[::-1]:
            max_r_score = cur
            

    return [-1] if max_r_score[-1] == -1 else max_r_score[:-1]

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))