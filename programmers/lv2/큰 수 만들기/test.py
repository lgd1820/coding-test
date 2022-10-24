def solution(number, k):
    answer = [number[0]]
    for n in number[1:]:
        while k > 0 and answer and answer[-1] < n:
            answer.pop()
            k -= 1
        
        answer.append(n)
    
    return ''.join(answer[:len(number) - k])

print(solution("1924", 2))
print(solution("1231234",3))
print(solution("4177252841",4))