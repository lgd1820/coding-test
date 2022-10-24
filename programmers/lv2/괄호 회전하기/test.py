def check(string):
    stack = []
    for char in string:
        if char in ["[", "(", "{"]:
            stack.append(char)
        else:
            if not stack: False
            x = stack.pop()
            if char == "]" and x != "[":
                return False
            elif char == ")" and x != "(":
                return False
            elif char == "}" and x != "{":
                return False

    if stack: return False
    return True

def solution(s):
    answer = 0
    s_list = []

    if len(s) % 2 == 1: return 0

    for i in range(0, len(s)):
        s_list.append(s[i:] + s[:i])

    for string in s_list:
        if check(string):
            answer += 1

    return answer

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("[{}]()"))