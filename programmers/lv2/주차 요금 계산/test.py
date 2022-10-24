import math

def solution(fees, records):
    answer = []
    dic = {}
    car_dic = {}
    for record in records:
        time, car_num, state = record.split()
        if not car_dic.get(car_num):
            car_dic[car_num] = 0

        if state == "IN":
            dic[car_num] = time
        else:
            in_hour, in_minute = dic[car_num].split(":")
            out_hour, out_minute = time.split(":")
            parking_time = (int(out_hour) * 60 + int(out_minute)) - (int(in_hour) * 60 + int(in_minute))
            dic.pop(car_num)
            car_dic[car_num] += parking_time

    for car_num, time in dic.items():
        in_hour, in_minute = dic[car_num].split(":")
        parking_time = 1439 - (int(in_hour) * 60 + int(in_minute))
        car_dic[car_num] += parking_time

    return [int(fees[1] + (math.ceil((time - fees[0]) / fees[2]) * fees[3])) if fees[0] < time else fees[1] for _, time in sorted(car_dic.items())]

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
