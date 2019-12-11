

def whatColor(_location, _hull):
    if _location not in _hull:
        return 0
    return _hull[_location]


def whatDirection(_location, turn, _orientation):
    if turn == 0:
        turn = -1
    if _orientation in ['u', 'd']:
        if _orientation == 'd':
            turn /= -1
        _location = (_location[0] + turn, _location[1])
        _orientation = 'r'
        if turn == -1:
            _orientation = 'l'
    elif _orientation in ['r', 'l']:
        if _orientation == 'r':
            turn /= -1
        _location = (_location[0], _location[1] + turn)
        _orientation = 'u'
        if turn == -1:
            _orientation = 'd'
    return _location, _orientation


def getValue(content, position, type, base):
    if type == 2:
        return base + content[position]
    if type == 1:
        return position
    return content[position]


def processOpCode(content, position, _base, _location, _hull, _first, _orientation):
    code = abs(content[position])
    operation = code
    first = 0
    second = 0
    third = 0
    new_position = 0
    _end = False
    if len(str(code)) > 2:
        operation = int(str(code)[-2:])
        if len(str(code)[:-2]) >= 1:
            first = int(str(code)[-3:-2])
        if len(str(code)[:-2]) >= 2:
            second = int(str(code)[-4:-3])
        if len(str(code)[:-2]) == 3:
            third = int(str(code)[-5:-4])
    try:
        if operation == 9:
            _base += content[getValue(content, position + 1, first, _base)]
            new_position = position + 2
        if operation == 8:
            if content[getValue(content, position + 1, first, _base)] == content[getValue(content, position + 2, second, _base)]:
                content[getValue(content, position + 3, third, _base)] = 1
            else:
                content[getValue(content, position + 3, third, _base)] = 0
            new_position = position + 4
        elif operation == 7:
            if content[getValue(content, position + 1, first, _base)] < content[getValue(content, position + 2, second, _base)]:
                content[getValue(content, position + 3, third, _base)] = 1
            else:
                content[getValue(content, position + 3, third, _base)] = 0
            new_position = position + 4
        elif operation == 6:
            if content[getValue(content, position + 1, first, _base)] == 0:
                new_position = content[getValue(content, position + 2, second, _base)]
            else:
                new_position = position + 3
        elif operation == 5:
            if content[getValue(content, position + 1, first, _base)] != 0:
                new_position = content[getValue(content, position + 2, second, _base)]
            else:
                new_position = position + 3
        elif operation == 4:
            new_position = position + 2
            if _first:
                _hull[_location] = content[getValue(content, position + 1, first, _base)]
                _first = False
            else:
                _location, _orientation = whatDirection(_location, content[getValue(content, position + 1, first, _base)], _orientation)
        elif operation == 3:
            new_position = position + 2
            _first = True
            content[getValue(content, position + 1, first, _base)] = whatColor(_location, _hull)
        elif operation == 2:
            new_position = position + 4
            content[getValue(content, position + 3, third, _base)] = content[getValue(content, position + 1, first, _base)] * \
                                                              content[getValue(content, position + 2, second, _base)]
        elif operation == 1:
            content[getValue(content, position + 3, third, _base)] = content[getValue(content, position + 1, first, _base)] + \
                                                              content[getValue(content, position + 2, second, _base)]
            new_position = position + 4

        if operation == 99:
            _end = True
    except IndexError:
        content += [0] * 4000
        return content, position, _end, _base, _location, _hull, _first, _orientation
    return content, new_position, _end, _base, _location, _hull, _first, _orientation


with open('file.in') as f:
    content = f.readlines()
content = [int(x) for x in content[0].split(",")]
#content = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
position = 0
original = content[:]
base = 0
print("Part 1")
end = False
location = (0, 0)
hull = {location: 0}
first = True
orientation = 'u'
while not end:
    content, position, end, base, location, hull, first, orientation = processOpCode(content, position, base, location, hull, first, orientation)
print(len(hull)) # Part 1
position = 0
original = content[:]
base = 0
end = False
location = (0, 0)
hull = {location: 1}
first = True
orientation = 'u'
while not end:
    content, position, end, base, location, hull, first, orientation = processOpCode(content, position, base, location, hull, first, orientation)
smallestx = 0
smallesty = 0
greatestx = 0
greatesty = 0
for key, _ in hull.iteritems():
    if key[0] < smallestx:
        smallestx = key[0]
    if key[0] > greatestx:
        greatestx = key[0]
    if key[1] < smallesty:
        smallesty = key[1]
    if key[1] > greatesty:
        greatesty = key[1]
rows = []
for y in range(smallesty, greatesty + 1):
    add_row = ''
    for x in range(smallestx, greatestx + 1):
        add_row += ' '
        if (x, y) in hull:
            if hull[(x, y)] == 1:
                add_row = add_row[:-1]
                add_row += 'W'
    rows.append(add_row)
rows.reverse()
print("Part 2")
for each in rows:
    print(each)
