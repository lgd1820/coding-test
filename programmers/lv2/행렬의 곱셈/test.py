def solution(arr1, arr2):
    answer = [[0 for i in range(len(arr2[0]))] for j in range(len(arr1))]
    row = len(arr2)
    col = len(arr2[0])
    arr2_t = [[0 for row in range(row)] for col in range(col)]
    
    for i in range(row):
        for j in range(col):
            arr2_t[j][i] = arr2[i][j]

    for i, arr1_row in enumerate(arr1):
        for j, arr2_row in enumerate(arr2_t):
            num = 0 
            for a, b in zip(arr1_row, arr2_row):
                num += a*b
            answer[i][j] = num

    return answer

print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))