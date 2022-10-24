from itertools import permutations

def solution(expression):
    answer = []

    priority = []
    split_ex = []

    num = ""
    for char in expression:
        if char.isdigit():
            num += char
        else:
            split_ex += [int(num)]
            num = ""
            split_ex += [char]
            if char not in priority:
                priority += [char]
    else:
        split_ex += [int(num)]

    priority = permutations(priority, len(priority))

    for p in priority:
        temp = split_ex[:]
        for formula in p:
            while formula in temp:
                index = temp.index(formula)
                if temp[index] == "+":
                    temp = temp[:index-1] + [temp[index-1] + temp[index+1]] + temp[index+2:]
                elif temp[index] == "-":
                    temp = temp[:index-1] + [temp[index-1] - temp[index+1]] + temp[index+2:]
                else:
                    temp = temp[:index-1] + [temp[index-1] * temp[index+1]] + temp[index+2:]
        answer.append(abs(temp[0]))
    return max(answer)


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
