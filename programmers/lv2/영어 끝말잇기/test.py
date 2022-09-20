import math

def solution(n, words):
    words_list = [words[0]]
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0]:
            return [i % n + 1, math.ceil((i + 1) / n)]
        elif words[i] in words_list:
            return [i % n + 1, math.ceil((i + 1) / n)]
        
        words_list.append(words[i])
        
    return [0, 0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
