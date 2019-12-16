import math


def determine_distance():
    count = 0
    levels = ['ORE']
    global reaction, distance
    distance['ORE'] = 0
    while True:
        count += 1
        level_add = []
        if not all([x in levels for x in all_keys]):
            for ele, react in reaction.iteritems():
                for i, spot in enumerate(react):
                    if spot[1] not in levels:
                        break
                    if i == len(react) - 1:
                        if ele not in levels:
                            distance[ele] = count
                            level_add.append(ele)
        else:
            break
        levels += level_add[:]


def compute_ore_needed(need):
    global distance, reaction, produced, one_fuel
    needed = {'FUEL': need}
    while True:
        max_distance = -1
        material = None
        for k, vals in needed.iteritems():
            if distance[k] > max_distance:
                max_distance = distance[k]
                material = k
        if material == 'ORE':
            if len(needed) > 1:
                continue
            else:
                if need == 1:
                    one_fuel = int(needed['ORE'])
                    print int(needed['ORE']) # Part 1
                    break
                return int(needed['ORE'])
        needed_q = math.ceil(needed[material] / produced[material])
        for each in reaction[material]:
            if each[1] not in needed:
                needed[each[1]] = 0
            needed[each[1]] += each[0] * needed_q
        del needed[material]


def how_much_fuel():
    global one_fuel
    ore = 1000000000000
    total = ore // one_fuel
    extra_ore = compute_ore_needed(total)
    while ore > extra_ore:
        total += (ore - extra_ore) // one_fuel + 1
        extra_ore = compute_ore_needed(total)
    print(total - 1) #part 2

with open('file.in') as f:
    content = f.readlines()
    distance = {}
    reaction = {}
    produced = {}
    all_keys = []
    one_fuel = None
    for row in content:
        row = row.replace(',', '')
        broken = row.split(' ')
        x = 0
        pairs = []
        while x < len(broken):
            if broken[x] != '=>':
                pairs.append((int(broken[x]), broken[x + 1]))
                x += 2
            else:
                x += 1
                reaction[broken[x + 1].replace('\n', '')] = pairs
                all_keys.append(broken[x + 1].replace('\n', ''))
                produced[broken[x + 1].replace('\n', '')] = int(broken[x])
                x += 2
    determine_distance()
    compute_ore_needed(1)
    how_much_fuel()
