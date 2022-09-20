def solution(id_list, report, k):
    dic = {id:0 for id in id_list}
    re_dic = {id:[] for id in id_list}

    for r in list(set(report)):
        rep = r.split()
        dic[rep[1]] += 1
        re_dic[rep[0]].append(rep[1])
    
    ban_list = [key for key, v in dic.items() if v >= k]

    answer = []
    for k, v in re_dic.items():
        mail = 0
        for ban_id in v:
            if ban_id in ban_list:
                mail += 1
        
        answer.append(mail)
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))