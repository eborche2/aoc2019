import math


def calculate_next(next_value):
    return -2 + math.floor(int(next_value) / 3)


with open('file.in') as f:
    content = f.readlines()
content = [x.strip() for x in content]
total_mass = 0
for each in content:
    total_mass += -2 + math.floor(int(each) / 3)
print(total_mass)  # Solution 1

total_mass = 0
for each in content:
    mass = calculate_next(each)
    total_mass += mass
    while mass > 0:
        mass = calculate_next(mass)
        if mass > 0:
            total_mass += mass
print(total_mass)  # Solution 2
