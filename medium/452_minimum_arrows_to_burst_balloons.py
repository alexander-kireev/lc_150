

def x(points):
    arrows = 1
    points.sort()
    START = 0
    END = 1

    last = points[0]

    for p in points[1:]:
        if p[START] <= last[END]:
            last[START] = max(p[START], last[START])
            last[END] = min(p[END], last[END])
        else:
            arrows += 1
            last = p
        
    return arrows




points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2

print(x(points))