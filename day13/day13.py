
def get_key(val):
    for key, value in locations.items():
        if val == value:
            return key
    return None


def breakout():
    if (x, y) == (-1, 0):
        scores.append(pin)
        print(pin)
        return
    if pin == 0:
        return
    if pin == 1:
        locations[(x, y)] = 'W'
        return
    if pin == 2:
        locations[(x, y)] = 'B'
        return
    if pin == 3:
        if get_key('P'):
            locations[get_key('P')] = ' '
        locations[(x, y)] = 'P'
        return
    if pin == 4:
        print((x,y))
        if (x, y) in locations:
            if locations[(x, y)] not in ['B', 'A', ' ']:
                return
        if get_key('A'):
            locations[get_key('A')] = ' '
        locations[(x, y)] = 'A'


def display():
    smallestx = 0
    smallesty = 0
    greatestx = 0
    greatesty = 0
    for key, _ in locations.iteritems():
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
            if (x, y) in locations:
                add_row = add_row[:-1]
                add_row += locations[(x, y)]
        rows.append(add_row)
    rows.reverse()
    print("Display")
    for each in rows:
        print(each)


def getValue(content, position, type, base):
    if type == 2:
        return base + content[position]
    if type == 1:
        return position
    return content[position]


def processOpCode(content, position, _base, _first, _second, _x, _y, _pin):
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
            if _second:
                if (_x, _y) == (-1, 0):
                    print (getValue(content, position + 1, first, _base))
                _pin = content[getValue(content, position + 1, first, _base)]
                _first = False
            elif _first:
                _y = content[getValue(content, position + 1, first, _base)]
                _second = True
            else:
                _x = content[getValue(content, position + 1, first, _base)]
                _first = True
        elif operation == 3:
            new_position = position + 2
            display()
            print("Joystick:")
            content[getValue(content, position + 1, first, _base)] = int(raw_input())
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
        return content, position, _end, _base, _first, _second, _x, _y, _pin
    return content, new_position, _end, _base, _first, _second, _x, _y, _pin


with open('file.in') as f:
    content = f.readlines()
content = [int(x) for x in content[0].split(",")]
position = 0
original = content[:]
x = 0
y = 0
pin = 0
base = 0
end, first, second = False, False, False
locations = {}
scores = []
while not end:
    content, position, end, base, first, second, x, y, pin = processOpCode(content, position, base, first, second, x, y, pin)
    if not first and second:
        second = False
        breakout()
count = 0
for each in locations:
    if locations[each] == 'B':
        count += 1
# print(count) Part 1 place a 1 in position 0, Part 2 place a 2 in position 0 and uncomment print statement.
