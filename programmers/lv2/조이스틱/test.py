# from itertools import permutations
from itertools import combinations

def solution(name):
    answer = 0
    min_move = len(name) - 1

    for i, char in enumerate(name):
        answer += min(ord(char) - 65, abs(26 - (ord(char) - 65)))
        idx = i + 1
        while idx < len(name) and name[idx] == 'A':
            idx += 1
        
        min_move = min([min_move, 2 *i + len(name) - idx, i + 2 * (len(name) - idx)])
    
    answer += min_move
    return answer
    # answer = 99999999999
    # char2int = [(i, min(ord(char) - 65, abs(26 - (ord(char) - 65)))) for i, char in enumerate(name)]
    # per = combinations(char2int, len(char2int))
    # for com in per:
    #     temp = 0
    #     temp_index = 0
    #     for i, tic in com:
    #         if tic == 0: continue
    #         temp += tic
            
    #         if abs(temp_index - i) > len(name) / 2:
    #             temp += len(name) - abs(temp_index - i)
    #         else:
    #             temp += abs(temp_index - i)
            
    #         temp_index = i

    #         if answer < temp:
    #             break
        
    #     if answer > temp:
    #         answer = temp
        
    # return answer

print(solution("JEROEN"))
print(solution("JAN"))
print(solution("A"))
print(solution("Z"))
print(solution("Y"))