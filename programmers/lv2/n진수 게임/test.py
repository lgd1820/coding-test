import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

def solution(n, t, m, p):
    answer = ''
    p_n = ""
    for i in range(t * m):
        p_n += convert(i, n)
    

    for i in range(t):
        answer += p_n[m * i + p - 1]
    return answer.upper()

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))