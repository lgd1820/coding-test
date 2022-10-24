class reversor:
    def __init__(self, obj):
        self.obj = obj

    def __eq__(self, other):
        return other.obj == self.obj

    def __lt__(self, other):
           return other.obj < self.obj

def solution(files):
    answer = []
    file = []
    for i, file_name in enumerate(files):
        head = ""
        number = ""
        tail = ""
        for j, c in enumerate(file_name):
            if not c.isnumeric():
                if not number:
                    head += c
                else:
                    tail = file_name[j:]
                    break
            else:
                number += c
        file.append((head, number, tail, i))
    answer = sorted(file, key=lambda x: (x[0].lower(), int(x[1]), x[3], x[2]))

    return ["".join(x[:3]) for x in answer]

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))