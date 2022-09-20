def solution(s):
    answer = [word.capitalize() for word in s.lower().split(' ')]
    return ' '.join(answer)

print(solution("3people       unFollowed me"))
print(solution("for the last week"))
print(solution("35people unFollowed me"))
print(solution("") + 'a')