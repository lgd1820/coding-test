from itertools import combinations

def solution(line):
    answer = []
    result = []
    comb = combinations(line, 2)
    min_x = 99999999
    min_y = 99999999
    max_x = -99999999
    max_y = -99999999

    for c in comb:
        a1, b1, c1 = c[0]
        a2, b2, c2 = c[1]

        if a1 * b2 - b1 * a2 != 0:
            x, y = (b1 * c2 - c1 * b2)/(a1 * b2 - b1 * a2), (c1 * a2 - a1 * c2) / (a1 * b2 - b1 * a2)
            if x == int(x) and y == int(y):
                x, y = int(x), int(y)

                if (x, y) not in result:
                    result.append((x, y))
                    min_x = min(min_x, x)
                    min_y = min(min_y, y)
                    max_x = max(max_x, x)
                    max_y = max(max_y, y)

    answer = [["."] * (abs(max_x - min_x) + 1) for _ in range(abs(max_y - min_y) + 1)]
    for r in result:
        x, y = abs(max_x - r[0]), abs(min_y - r[1])
        answer[y][x] = "*"
    
    return ["".join(a) for a in answer][::-1]

# def solution(line):
    # star_list = []
    # for i in range(len(line)):
    #     for j in range(i+1,len(line)):
    #         a, b, e = line[i]
    #         c, d, f = line[j]
    #         if a*d - b*c !=0:
    #             x,y = (b*f-e*d)/(a*d - b*c) , (e*c-a*f)/(a*d - b*c)
    #             if x.is_integer() and y.is_integer():
    #                 x,y = int(x),int(y)
    #                 if (x,y) not in star_list:
    #                     star_list.append((x,y))
    # x_min, x_max, y_min, y_max = min(star_list)[0],max(star_list)[0],min(star_list,key = lambda x: x[1])[1],max(star_list,key = lambda x: x[1])[1]
    # star = [['.']*(abs(x_max-x_min)+1) for _ in range((abs(y_max-y_min)+1))]
    # for s in star_list:
    #     a,b = s
    #     x,y = abs(y_max-b) , abs(x_min-a)
    #     star[x][y] = '*'
    # for i,v in enumerate(star):
    #     star[i] = ''.join(v)
    # return star

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[1, -1, 0], [2, -1, 0]]))
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))