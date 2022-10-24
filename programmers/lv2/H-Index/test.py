def solution(citations):
    citations.sort()
    article_count = len(citations)

    for i in range(article_count):
        if citations[i] >= article_count - i:
            return article_count - i
    return 0

print(solution([3, 0, 6, 1, 5]))
print(solution([1 for _ in range(1000)]))