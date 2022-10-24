import heapq

def solution(N, road, K):
    INF = int(1e9)
    num_downtown = len(set([a for a, b, w in road] + [b for a, b, w in road])) + 1
    distance = [INF] * num_downtown
    distance[1] = 0
    graph = [[] for _ in range(num_downtown)]

    for a, b, w in road:
        graph[a].append((b,w))
        graph[b].append((a,w))

    queue = []
    heapq.heappush(queue, (distance[1], 1))

    while queue:
        cur_distance, node = heapq.heappop(queue)
        if distance[node] < cur_distance:
            continue
        
        for n, w in graph[node]:
            w_distance = cur_distance + w
            if w_distance < distance[n]:
                distance[n] = w_distance
                heapq.heappush(queue, (w_distance, n))
    return len([True for d in distance if d <= K])


print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)) # 4
print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4)) # 4