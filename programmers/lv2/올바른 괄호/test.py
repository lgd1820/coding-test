def solution(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif len(stack) and c == ")":
            stack.pop()
        else:
            return False
    
    return False if len(stack) else True
            


print(solution("(())()"))
print(solution(")()("))