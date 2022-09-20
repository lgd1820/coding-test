def solution(arr):
    total_num_list = [ 0 for _ in range(max(arr) + 1)]
    for num in arr:
        multi = 2
        num_list = [0 for _ in range(max(arr) + 1)]
        while multi <= num:
            if num % multi == 0:
                num = num / multi
                num_list[multi] += 1
            else:
                multi += 1
        
        total_num_list = [ a if a > b else b for a, b in zip(total_num_list, num_list)]
    
    answer = 1
    for i, num in enumerate(total_num_list):
        if num != 0:
            answer = answer * (i  ** num)
    return answer

print(solution([2,6,8,14]))
print(solution([1,2,3]))