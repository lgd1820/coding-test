from collections import deque

def solution(n, roads, sources, destination):
    road_map = dict()
    for road in roads:
        if road_map.get(road[0]):
            road_map[road[0]].append(road[1])
        else:
            road_map[road[0]] = [road[1]]
        if road_map.get(road[1]):
            road_map[road[1]].append(road[0])
        else:
            road_map[road[1]] = [road[0]]

    queue = deque([destination])
    visited = [-1] * (n+1)
    visited[destination] = 0
    while queue:
        v = queue.popleft()
        for node in road_map[v]:
            if visited[node] == -1:
                visited[node] = visited[v] + 1
                queue.append(node)

    return [visited[source] for source in sources]

print(solution(3,[[1, 2], [2, 3]],[2, 3],1))
print(solution(5,[[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]],[1, 3, 5],5))