from collections import defaultdict
from itertools import combinations

def compare(start, end, target_list, target):
    if start >= end:
        return start
    
    mid = (start + end) // 2

    if target_list[mid] >= target:
        return compare(start, mid, target_list, target)
    else:
        return compare(mid+1, end, target_list, target)

def solution(info, query):
    answer = []

    dic = defaultdict(list)
    
    for info_s in info:
        ifs = info_s.split()
        status = ifs[:-1] 
        score = int(ifs[-1])

        for i in range(5):
            case = list(combinations([0, 1, 2, 3], i))
            for c in case:
                temp = status.copy() 
                for idx in c:
                    temp[idx] = "-"
                dic["".join(temp)].append(score)
    
    for value in dic.values():
        value.sort()  

    for qs in query:
        qs = qs.replace("and ", "").split()
        qs_str = "".join(qs[:-1])
        qs_score = int(qs[-1])
        count = 0
        if qs_str in dic:
            target_list = dic[qs_str]
            count = len(target_list) - compare(0, len(target_list), target_list, qs_score)
        answer.append(count)
        
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))