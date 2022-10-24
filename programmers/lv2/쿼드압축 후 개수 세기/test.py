results = []

def division(arr, x, y, size):
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != arr[x][y]:
                size //= 2
                division(arr, x, y, size)
                division(arr, x, y + size, size)
                division(arr, x + size, y, size)
                division(arr, x + size, y + size, size)
                return

    results.append(arr[x][y])

def solution(arr):
    results.clear()
    div = len(arr)
    division(arr, 0, 0, div)

    return [results.count(0), results.count(1)]


print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))