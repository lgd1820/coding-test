def uv(str):
    dic = {"(" : 0, ")" : 0}

    for i, char in enumerate(str):
        dic[char] += 1
    
        if dic["("] == dic[")"]:
            return str[:i+1], str[i+1:]

def is_balance(str):
    stack = []
    for char in str:
        if char == "(":
            stack += [char]
        else:
            if not stack:
                return False
            stack.pop()
    
    return False if stack else True
        

def solution(p):
    if not p:
        return p
    
    u, v = uv(p)
    
    if is_balance(u):
        return u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"

        for pp in u[1:len(u) - 1]:
            if pp == "(":
                answer += ")"
            else:
                answer += "("

    return answer
    

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))