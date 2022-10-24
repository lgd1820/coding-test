def solution(msg):
    dic = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    answer = []

    w, c = 0, 0

    while True:
        c += 1
        if c == len(msg):
            answer.append(dic.index(msg[w:c]) + 1)
            break
    
        if msg[w:c+1] not in dic:
            dic.append(msg[w:c+1])
            answer.append(dic.index(msg[w:c]) + 1)
            w = c
    
    return answer

print(solution("KAKAO"))