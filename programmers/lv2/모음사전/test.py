def solution(word):
    dic = ["A", "E", "I", "O", "U"]
    answer = 0
    temp = ""
    while temp != word:
        if len(temp) < 5:
            temp += "A"
        else:
            if temp[-1] == "U":
                while temp[-1] == "U":
                    temp = temp[:-1]
                
            temp =  temp[:-1] + dic[dic.index(temp[-1])+1]

        answer += 1
    return answer

print(solution("AAAAE"))
print(solution("AAAE"))