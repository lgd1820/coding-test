def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0: return len(cities) * 5
    for city in cities:
        city = city.lower()
        if not city in cache:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.pop(0)
                cache.append(city)
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            answer += 1
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))