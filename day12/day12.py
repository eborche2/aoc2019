from itertools import combinations


def adjust_velocity(moon_pair):
    first_moon = moon_pair[0]
    second_moon = moon_pair[1]
    for x in range(3):
        if first_moon['p'][-1][x] > second_moon['p'][-1][x]:
            first_moon['v'][-1][x] -= 1
            second_moon['v'][-1][x] += 1
        elif first_moon['p'][-1][x] < second_moon['p'][-1][x]:
            first_moon['v'][-1][x] += 1
            second_moon['v'][-1][x] -= 1
    return first_moon, second_moon


def adjust_position(_moon):

    for x in range(3):
        _moon['p'][-1][x] += _moon['v'][-1][x]
    _moon['p'][-1] = tuple(moon['p'][-1])
    _moon['v'][-1] = tuple(moon['v'][-1])
    return _moon


def check_duplicate(_moons):
    for m in _moons:
        if len(m['p']) == len(set(m['p'])):
            return False
    return True


Io = {
    'p': [[-4, 3, 15]],
    'v': [[0, 0, 0]]
}
Europa = {
    'p': [[-11, -10, 13]],
    'v': [[0, 0, 0]]
}
Ganymede = {
    'p': [[2, 2, 18]],
    'v': [[0, 0, 0]]
}
Callisto = {
    'p': [[7, -1, 0]],
    'v': [[0, 0, 0]]
}

moons = [Io, Europa, Ganymede, Callisto]
original = moons[:]
for x in range(1000):
    for moon in moons:
        moon['p'].append(list(moon['p'][-1][:]))
        moon['v'].append(list(moon['v'][-1][:]))
    for pair in combinations(moons, 2):
        moons[moons.index(pair[0])], moons[moons.index(pair[1])] = adjust_velocity(pair)
    for i, moon in enumerate(moons):
        moons[i] = adjust_position(moon)
total_energy = 0
for moon in moons:
    print(moon['v'][-1])
    print(moon['p'][-1])
    vel = [abs(x) for x in moon['v'][-1]]
    pos = [abs(x) for x in moon['p'][-1]]
    total_energy += sum(vel) * sum(pos)
print(total_energy) #part 1

found_duplicate = False
moons = original
steps = 0
for moon in moons:
    moon['p'][0] = tuple(moon['p'][0])
    moon['v'][0] = tuple(moon['v'][0])
while not found_duplicate:
    steps += 1
    for moon in moons:
        moon['p'].append(list(moon['p'][-1][:]))
        moon['v'].append(list(moon['v'][-1][:]))
    for pair in combinations(moons, 2):
        moons[moons.index(pair[0])], moons[moons.index(pair[1])] = adjust_velocity(pair)
    for i, moon in enumerate(moons):
        moons[i] = adjust_position(moon)
    found_duplicate = check_duplicate(moons)
    if moons[0]['p']
print(steps) # part 2