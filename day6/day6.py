#python3.7


def check_match(_locations, orbit):
    if orbit[:3] in _locations:
        return True
    return False


def process_orbit(_locations, _orbit_map, _total_orbits, _count):
    new_locations = []
    to_remove = []
    _count += 1
    orbits_found = 0
    for i, orbit in enumerate(_orbit_map):
        if check_match(_locations, orbit):
            new_locations.append(orbit[4:7])
            orbits_found += 1
            to_remove.append(orbit)
    _total_orbits += orbits_found * _count
    _orbit_map = list(set(_orbit_map) - set(to_remove))
    return new_locations, _orbit_map, _total_orbits, _count


def find_next(location, _orbit_map):
    for orbit in _orbit_map:
        if orbit[4:7] == location:
            return orbit[:3]


def work_backwards(_locations_san, _locations_you, _orbit_map):
    if _locations_san[0] != 'COM':
        _locations_san.insert(0, find_next(_locations_san[0], _orbit_map))
    if _locations_you[0] != 'COM':
        _locations_you.insert(0, find_next(_locations_you[0], _orbit_map))
    return _locations_san[0] == 'COM' and _locations_you[0] == 'COM', _locations_san, _locations_you


with open('file.in') as f:
    orbit_map = f.readlines()
original_map = orbit_map[:]
total_orbits = 0
count = 0
locations = ["COM"]

while len(orbit_map) > 0:
    locations, orbit_map, total_orbits, count = process_orbit(locations, orbit_map, total_orbits, count)
print(total_orbits) #part 1

origin = False
locations_san = ['SAN']
locations_you = ['YOU']
while not origin:
    origin, locations_san, locations_you = work_backwards(locations_san, locations_you, original_map)
found_you = 0
found_san = 0
for i, location in enumerate(locations_you):
    for z, location_match in enumerate(locations_san):
        if location == location_match:
            if found_you + found_san < i + z:
                found_you = i
                found_san = z
locations_you = locations_you[found_you:]
locations_san = locations_san[found_san:]
print(len(locations_you) + len(locations_san) - 4) # part 2
