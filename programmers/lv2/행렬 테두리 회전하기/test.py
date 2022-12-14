def solution(rows, columns, queries):
    answer = []
    matrix = [ [i*columns+ j for j in range(1, columns+1)] for i in range(rows)]
    

    for query in queries:
        query = [x-1 for x in query] # 0부터 시작하는 인덱스에 맞춰 1씩 빼줌
        tmp = matrix[query[0]][query[1]] # 왼쪽 위 값 저장
        small = tmp
        
        # left
        for i in range(query[0]+1, query[2]+1):
            matrix[i-1][query[1]] = matrix[i][query[1]]
            small = min(small, matrix[i][query[1]])
        # bottom
        for i in range(query[1]+1, query[3]+1):
            matrix[query[2]][i-1] = matrix[query[2]][i]
            small = min(small, matrix[query[2]][i])
        # right
        for i in range(query[2]-1, query[0]-1, -1):
            matrix[i+1][query[3]] = matrix[i][query[3]]
            small = min(small, matrix[i][query[3]])
        # top
        for i in range(query[3]-1, query[1]-1, -1):
            matrix[query[0]][i+1] = matrix[query[0]][i]
            small = min(small, matrix[query[0]][i])
        matrix[query[0]][query[1]+1] = tmp
        
        answer.append(small)
            
    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# print(solution(6,7,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))