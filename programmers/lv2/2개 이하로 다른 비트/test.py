def solution(numbers):
    answer = []
    for num in numbers:
        bin_num = "0" + bin(num)[2:]
        index = bin_num.rfind("0")
        bin_num = bin_num[:index] + "1" + bin_num[index+1:]

        if num % 2 == 1:
            bin_num = bin_num[:index+1] + "0" + bin_num[index+2:]
        
        answer.append(int(bin_num, 2))
    return answer

print(solution([2,7]))
print(solution([11, 12345]))