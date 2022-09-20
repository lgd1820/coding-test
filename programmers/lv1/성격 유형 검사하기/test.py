def solution(survey, choices):
    dic = {
        "R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0
    }
    
    for (c1, c2), score in zip(survey, choices):
        score = score - 4
        if score > 0:
            dic[c2] += score
        else:
            dic[c1] += -1 * score
    
    answer = ''
    if dic["R"] >= dic["T"]:
        answer += "R"
    else:
        answer += "T"
    
    if dic["C"] >= dic["F"]:
        answer += "C"
    else:
        answer += "F"

    if dic["J"] >= dic["M"]:
        answer += "J"
    else:
        answer += "M"

    if dic["A"] >= dic["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))