def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        s = skill
        for c in skill_tree:
            if s:
                if c == s[0]:
                    s = s[1:]
                else:
                    if c in s:
                        answer += -1
                        break
            else:
                break
        
        answer += 1

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
print(solution("C", ["C"]))