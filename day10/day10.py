from fractions import gcd


def determine_quadrant(base, asteroid):
    right = False
    up = False
    if asteroid[0] >= base[0]:
        right = True
    if asteroid[1] >= base[1]:
        up = True
    if right and up:
        return 0
    if up:
        return 1
    if right:
        return 2
    return 3


def check_sight(_quadrant, _base_loc, _ast_loc):
    distance = (_base_loc[0] - _ast_loc[0], _base_loc[1] - _ast_loc[1])
    is_blocked = False
    lcm = gcd(abs(distance[0]), abs(distance[1]))
    distance = (distance[0] // lcm, distance[1] // lcm)
    if distance in _quadrant:
        is_blocked = True
    if not is_blocked:
        _quadrant.append(distance)
    return _quadrant, is_blocked


with open('file.in') as f:
    content = f.readlines()
asteroid_map = {}
for y, each in enumerate(content):
    for x, loc in enumerate(each):
        if loc == '#':
            asteroid_map[(x, y)] = '#'

largest = 0
largest_point = ''
largest_quadrants = None
for base_loc, asteroid in asteroid_map.items():
    count = 0
    quadrants = []
    [quadrants.append([]) for x in range(4)]
    for ast_loc, _ in asteroid_map.items():
        if base_loc == ast_loc:
            continue
        quadrant = determine_quadrant(base_loc, ast_loc)
        quadrants[quadrant], blocked = check_sight(quadrants[quadrant], base_loc, ast_loc)
        if not blocked:
            count += 1
    if count > largest:
        largest = count
        largest_point = base_loc
        largest_quadrants = quadrants
    asteroid_map[base_loc] = count
print(largest, largest_point)# Part 1
count_200 = 0
quadrant_200_in = None
before_quadrant = 0
for x in [1, 3, 2, 0]:
    print(quadrants[x])
    for _ in largest_quadrants[x]:
        count_200 += 1
        if count_200 == 200:
            quadrant_200_in = x
    if not quadrant_200_in:
        before_quadrant += len(largest_quadrants[x])
slope = {}
slopes = []
for point in largest_quadrants[quadrant_200_in]:
    slopes.append(float(point[0]) / float(point[1]))
    slope[slopes[-1]] = point
slopes.sort()
number_200 = 0
for sl in slopes:
    before_quadrant += 1
    if before_quadrant == 200:
        number_200 = slope[sl]
        break
possible_points = []
for ast_loc, _ in asteroid_map.items():
    if largest_point != ast_loc:
        distance = (largest_point[0] - ast_loc[0], largest_point[1] - ast_loc[1])
        lcm = gcd(abs(distance[0]), abs(distance[1]))
        distance_least = (distance[0] // lcm, distance[1] // lcm)
        if distance_least == number_200:
            possible_points.append(ast_loc)
print(ast_loc) # Part2 Choose the one closest to largest_point if there are more than 1








