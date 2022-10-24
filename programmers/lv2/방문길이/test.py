def solution(dirs):
    answer = 0
    x = 0
    y = 0
    move = []
    for d in dirs:
        p_x = x
        p_y = y
        if d == "U":
            if y != 5:
                y += 1
        elif d == "L":
            if x != -5:
                x -= 1
        elif d == "R":
            if x != 5:
                x += 1
        elif d == "D":
            if y != -5:
                y -= 1

        if p_x == x and p_y == y: continue

        if not (p_x, p_y, x, y) in move:
            answer += 1

        move.append((p_x, p_y, x, y))
        move.append((x, y, p_x, p_y))
    return answer

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))