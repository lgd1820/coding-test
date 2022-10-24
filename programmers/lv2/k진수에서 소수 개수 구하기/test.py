import string
import math

tmp = string.digits+string.ascii_lowercase

def convert(n, k):
    q, r = divmod(n, k)
    if q == 0:
        return tmp[r] 
    else :
        return convert(q, k) + tmp[r]

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    
    return True

def solution(n, k):
    answer = 0
    k_num = convert(n, k)
    
    num_list = [ int(i) for i in k_num.split('0') if i and i > "1"]

    for num in num_list:
        if is_prime_number(num):
            answer += 1

    return answer

print(solution(437674, 3))
print(solution(110011, 10))
print(solution(3, 3))