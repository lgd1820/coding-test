dic = {
    "zero" : "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def solution(s):
    for word, num in dic.items():
        s = s.replace(word, num)
    return s

print(solution("one4seveneight"))