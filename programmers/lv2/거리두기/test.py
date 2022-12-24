def solution(places):
    answer = []

    for place in places:
        p_list = [(y, x) for y in range(5) for x in range(5) if place[y][x] == 'P']

        flag = True
        for y1, x1 in p_list:
            for y2, x2 in p_list:
                if not flag: continue
                dist = abs(y2-y1) + abs(x2-x1)
                if dist == 0 or dist > 2:
                    continue

                if dist == 1:
                    flag = False
                elif y1 == y2 and place[y1][int((x1+x2)/2)] != 'X':
                    flag = False
                elif x1 == x2 and place[int((y1+y2)/2)][x1] != 'X':
                    flag = False
                elif y1 != y2 and x1 != x2:
                    if place[y2][x1] != 'X' or place[y1][x2] != 'X':
                        flag = False
        if flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))