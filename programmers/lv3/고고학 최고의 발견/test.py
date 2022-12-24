def solution(clockHands):
    answer = 0

    while True:
        flag = False
        max_count = 0
        max_i = 0
        max_j = 0
        for i, ch in enumerate(clockHands):
            for j, num in enumerate(ch):
                count = 0
                if num != 3:
                    count += 1

                if i == 0:
                    if clockHands[i+1][j] != 0:
                        count += 1
                elif i == len(clockHands) - 1:
                    if clockHands[i-1][j] != 0:
                        count += 1
                else:
                    if clockHands[i+1][j] != 0:
                        count += 1
                    if clockHands[i-1][j] != 0:
                        count += 1
               
                if j == 0:
                    if clockHands[i][j+1] != 0:
                        count += 1
                elif j == len(ch) - 1:
                    if clockHands[i][j-1] != 0:
                        count += 1
                else:
                    if clockHands[i][j+1] != 0:
                        count += 1
                    if clockHands[i][j-1] != 0:
                        count += 1
                
                if count == 5:
                    clockHands[i][j] = 0
                    clockHands[i+1][j] = 0
                    clockHands[i-1][j] = 0
                    clockHands[i][j+1] = 0
                    clockHands[i][j-1] = 0
                    break

                if max_count < count:
                    max_i = i
                    max_j = j
                    max_count = count



        clockHands[max_i][max_j] = 0
        if max_i == 0:
            clockHands[max_i+1][max_j] = 0
        elif max_i == len(clockHands) - 1:
            clockHands[max_i-1][max_j] = 0
        else:
            clockHands[max_i+1][max_j] = 0
            clockHands[max_i-1][max_j] = 0

        if max_j == 0:
            clockHands[max_i][max_j+1] = 0
        elif max_j == len(clockHands[0]) - 1:
            clockHands[max_i][max_j-1] = 0
        else:
            clockHands[max_i][max_j+1] = 0
            clockHands[max_i][max_j-1] = 0

        if max_count == 0 and max_i == 0 and max_j == 0:
            return 0
        answer += 1

        for ch in clockHands:
            if ch.count(0) != len(ch):
                break
            else:
                flag = True
        else:
            flag = False

        if flag:
            answer += 1
            break

    return answer

print(solution([[0,3,3,0],[3,2,2,3],[0,3,2,0],[0,3,3,3]]))