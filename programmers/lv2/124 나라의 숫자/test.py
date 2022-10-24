import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

# def convert(n):
#     T = "124"
#     q, r = divmod(n,3)
#     if q == 0:
#         return T[r-1]
#     else:
#         return T[q-1] + convert(r)

def solution(n):
    answer = ""

    while n:
        if n % 3:
            answer += str(n % 3)
            n = n // 3
        else:
            answer += "4"
            n = n // 3 - 1
    return answer[::-1]


for i in range(1, 11):
    print(solution(i))