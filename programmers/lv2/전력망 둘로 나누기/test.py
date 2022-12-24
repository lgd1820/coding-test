from collections import defaultdict, deque

def solution(n, wires):
    answer = 999999999999

    data = defaultdict(set)
    for a, b in wires:
        data[a].add(b)
        data[b].add(a)

    for wire in wires:
        count = 1
        visitied = [False] * (n + 1)
        visitied[wire[0]] = True
        queue = deque([wire[0]])

        while queue:
            cur = queue.popleft()
            for i in data[cur]:
                if visitied[i] or i == wire[1]:
                    continue
                count += 1
                queue.append(i)
                visitied[i] = True
        
        answer = min(answer, abs(n-count-count))

    return answer

print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4,[[1,2],[2,3],[3,4]]))
print(solution(7,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))