from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for perm in permutations(dungeons, len(dungeons)):
        fatigue = k
        count = 0
        for pm in perm:
            if fatigue >= pm[0]:
                fatigue -= pm[1]
                count +=1
            if count > answer:
                answer = count
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))