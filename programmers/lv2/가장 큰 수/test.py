class reversor:
    def __init__(self, obj):
        self.obj = obj

    def __eq__(self, other):
        return other.obj == self.obj

    def __lt__(self, other):
           return other.obj < self.obj

def solution(numbers):
    strings_ints = [str(number) for number in numbers]
    if len(''.join(strings_ints)) == ''.join(strings_ints).count("0"):
        return "0"
    return ''.join(sorted(strings_ints, key=lambda x: x * 3, reverse=True))


print(solution([6, 10, 2]))

print(solution([3, 30, 34, 5, 9]))
print(solution([232,23]))
print(solution([212,21]))
print(solution([70,0,0,0,0]))
print(solution([9, 998]))
print(solution([101, 10, 232, 23])) 