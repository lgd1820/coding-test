def solution(s):
    zero = 0
    count = 0
    while s != "1":
        zero += s.count("0")
        count += 1
        s = bin(len(s.replace("0", "")))[2:]
    return [count, zero]


print(solution("110010101001"))