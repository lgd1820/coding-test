def solution(w,h):
    x, y = w, h
    while y:
        x, y = y, x % y
    
    return w * h - (w + h - x)

print(solution(8, 12))


# def solution(w,h):
#     x1, x2 = 0, w
#     y1, y2 = 0, -1 * h
#     dx = x2 - x1
#     dy = y2 - y1
    
#     is_steep = abs(dy) - abs(dx)

#     if is_steep:
#         x1, y1 = y1, x1
#         x2, y2 = y2, x2

#     swapped = False
#     if x1 > x2:
#         x1, x2 = x2, x1
#         y1, y2 = y2, y1
#         swapped = True
        
#     dx = x2 - x1
#     dy = y2 - y1

#     err = dx // 2
#     y_step = 1 if y1 < y2 else -1
    
#     y = y1
#     path = []
#     for x in range(x1, x2+1):
#         coord = (y, x) if is_steep else (x, y)
#         path.append(coord)
#         err -= abs(dy)
#         if err < 0:
#             y += y_step
#             err += dx
    
#     if swapped:
#         print(list(reversed(path)))
#     else:
#         print(path)
        
#     return -1