def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_set = [ str1[i-1] + str1[i] for i in range(1, len(str1)) if str1[i-1].isalpha() and str1[i].isalpha()]
    str2_set = [ str2[i-1] + str2[i] for i in range(1, len(str2)) if str2[i-1].isalpha() and str2[i].isalpha()]

    answer = 0

    temp = str1_set.copy()
    union = str1_set.copy()
    intersection = []

    for element in str2_set:
        if element in temp:
            temp.remove(element)
            intersection.append(element)
        else:
            union.append(element)

    if not union: return 65536
    return int((len(intersection) / len(union)) * 65536)

print(solution("FRANCE","french"))
print(solution("handshake","shake hands"))
print(solution("aa1+aa2","AAAA12"))
print(solution("E=M*C^2","e=m*c^2"))