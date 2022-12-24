from itertools import combinations

def solution(relation):
    n = len(relation[0])
    idx = list(range(n))
    candidate_key = []

    for i in range(1, n+1):
        for comb in combinations(idx, i):
            hist = []
            for r in relation:
                cur_key = [r[c] for c in comb]
                if cur_key in hist:
                    break
                else:
                    hist.append(cur_key)
            else:
                for ck in candidate_key:
                    if set(ck).issubset(set(comb)):
                        break
                else:
                    candidate_key.append(comb)
    return len(candidate_key)
    # answer = 0

    # dic = {}
    # r_key = []

    # for r in relation:
    #     for i, e in enumerate(r):
    #         if dic.get(i):
    #             dic[i].append(e)
    #         else:
    #             dic[i] = [e]
        
    # for k, v in dic.items():
    #     if len(set(v)) == len(relation):
    #         answer += 1
    #         r_key.append(k)

    # for i in range(2, len(dic) - len(r_key)):
    #     s = [k for k in dic.keys() if k not in r_key]
    #     com = list(combinations(s, i))
    #     for c in com:
    #         l = []
    #         for r in relation:
    #             l.append(tuple([r[j] for j in c]))
    #         if len(set(l)) == len(relation):
    #             answer += 1
    #             r_key += [j for j in c]

    # return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))