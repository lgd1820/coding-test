def solution(m, musicinfos):
    dic = {
        "C#": "H",
        "D#": "I",
        "F#": "J",
        "G#": "K", 
        "A#": "L"
    }

    answer = []
    for i, musicinfo in enumerate(musicinfos):
        mi = musicinfo.split(",")
        start = [int(t) for t in mi[0].split(":")]
        end = [int(t) for t in mi[1].split(":")]
        time = (end[0] * 60 + end[1]) - (start[0] * 60 + start[1])
        melody = mi[3] * (time // len(mi[3])) + mi[3][:(time % len(mi[3]))]
        for k, v in dic.items():
            melody = melody.replace(k, v)
            m = m.replace(k, v)

        if m in melody:
            answer.append((mi[2], time, i))

    if answer:
        return sorted(answer, key=lambda x: -x[1])[0][0]
    else:
        return "(None)"

def solution(m, musicinfos):
    answer = []
    m = m.replace('A#', 'H').replace('C#', 'I').replace('D#', 'J').replace('F#', 'K').replace('G#', 'L')

    for musicinfo in musicinfos:
        musicinfo = musicinfo.split(',')
        musicinfo[3] = musicinfo[3].replace('A#', 'H').replace('C#', 'I').replace('D#', 'J').replace('F#', 'K').replace(
            'G#', 'L')

        time = (int(musicinfo[1].split(':')[0]) * 60 + int(musicinfo[1].split(':')[1])) - (
                    int(musicinfo[0].split(':')[0]) * 60 + int(musicinfo[0].split(':')[1]))

        music = ''.join(musicinfo[3] * (time // len(musicinfo[3])) + musicinfo[3][:time % len(musicinfo[3])])

        if m in music:
            answer.append((time, musicinfo[2]))

    if len(answer) > 0:
        answer.sort(key=lambda x: -x[0])
        return answer[0][1]

    return "(None)"

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))