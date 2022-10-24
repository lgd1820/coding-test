def solution(want, number, discount):
    answer = 0
    for i in range(0, len(discount) - 9):
        ten = discount[i:i+10]
        for j, want_product in enumerate(want):
            if ten.count(want_product) < number[j]:
                break
        else:
            answer += 1
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"],[10],["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))