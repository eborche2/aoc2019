

def getValue(content, position, type, base):
    if type == 2:
        return base + content[position]
    if type == 1:
        return position
    return content[position]


def processOpCode(content, position, _base):
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
            print("OutputCode: ", content[getValue(content, position + 1, first, _base)], position, code,
                  getValue(content, position + 1, first, _base))
        elif operation == 3:
            new_position = position + 2
            print("Input number:")
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
        return content, position, _end, _base
    return content, new_position, _end, _base


with open('file.in') as f:
    content = f.readlines()
content = [int(x) for x in content[0].split(",")]
#content = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
position = 0
original = content[:]
base = 0
print("Part 1 and 2")
end = False
while not end:
    content, position, end, base = processOpCode(content, position, base)
