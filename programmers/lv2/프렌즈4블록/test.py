def solution(m, n, board):
    answer = 0
    temp = board[:]
    delete_list = []

    while True:
        for i, row in enumerate(temp[:-1]):
            for j, c in enumerate(row[:-1]):
                if c == "-": continue
                if temp[i+1][j+1] == c:
                    if temp[i+1][j] == c and temp[i][j+1] == c:
                        delete_list.append((i, j))
            
        if not delete_list:
            break
    
        for i, j in delete_list:
            temp[i] = temp[i][:j] + "--" + temp[i][j+2:]
            temp[i+1] = temp[i+1][:j] + "--" + temp[i+1][j+2:]
        delete_list.clear()


        temp = list(map(list, zip(*temp)))

        for i, row in enumerate(temp):
            count = 0
            stack = ""
            for c in row:
                if c == "-":
                    count += 1
                else:
                    stack += c
                
            stack = count * "-" + stack
            temp[i] = stack

        temp = list(map(list, zip(*temp)))
        temp = [''.join(row) for row in temp]

    for t in temp:
        answer += t.count("-")

    return answer

"""
TTTANT
RRFACC
RRRFCC
TRRRAA
TTMMMF
TMMTTJ
"""

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))