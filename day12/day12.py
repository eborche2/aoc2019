from itertools import combinations
import copy

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


def _adjust_velocity(_new_pos, _new_vel, pos):
    compared = [0]
    for x, first in enumerate(_new_pos):
        compared.append(x)
        for z, second in enumerate(_new_pos):
            if z in compared:
                continue
            if first[pos] > second[pos]:
                _new_vel[x][pos] -= 1
                _new_vel[z][pos] += 1
            elif first[pos] < second[pos]:
                _new_vel[x][pos] += 1
                _new_vel[z][pos] -= 1
    return _new_vel


def  _adjust_position(_new_pos, pos):
    for i, moon in enumerate(_new_pos):
        _new_pos[i][pos] = moon[pos] + new_vel[i][pos]
    return _new_pos


def check(position):
    for i in range(4):
        if pos[i][position] != new_pos[i][position]:
            return False
        if vel[i][position] != new_vel[i][position]:
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
original = copy.deepcopy(moons)
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
    vel = [abs(x) for x in moon['v'][-1]]
    pos = [abs(x) for x in moon['p'][-1]]
    total_energy += sum(vel) * sum(pos)
print(total_energy) #part 1

pos = [[-4, 3, 15], [-11, -10, 13], [2, 2, 18], [7, -1, 0]]
vel = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
path = [0, 0, 0]
new_pos = copy.deepcopy(pos)
new_vel = copy.deepcopy(vel)

# borrowed from https://www.w3resource.com/python-exercises/challenges/1/python-challenges-1-exercise-37.php
def gcd(x, y):
    return y and gcd(y, x % y) or x


def lcm(x, y):
    return x * y / gcd(x, y)


for position in range(3):
    found = False
    print("here")
    while not found:
        path[position] += 1
        new_vel = _adjust_velocity(new_pos, new_vel, position)
        new_pos = _adjust_position(new_pos, position)
        found = check(position)
n = path[0]
for i in path:
    n = lcm(n, i)
print(n) # Part 2 :(

