def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    while bridge:
        if len(bridge) < bridge_length:
            if truck_weights:
                if sum(bridge) + truck_weights[0] <= weight:
                    truck = truck_weights.pop(0)
                    bridge += [truck]
                else:
                    bridge += [0]
            else:
                answer += len(bridge)
                break
        bridge.pop(0)
        answer += 1

    return answer

print(solution(2, 10, [7,4,5,6]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))