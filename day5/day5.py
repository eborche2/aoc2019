def getValue(content, position, type):
    if type == 1:
        return position
    return content[position]


def processOpCode(content, position):
    code = abs(content[position])
    operation = code
    first = 0
    second = 0
    third = 0
    new_position = 0
    if len(str(code)) > 2:
        operation = int(str(code)[-2:])
        if len(str(code)[:-2]) >= 1:
            first = int(str(code)[-3:-2])
        if len(str(code)[:-2]) >= 2:
            second = int(str(code)[-4:-3])
        if len(str(code)[:-2]) == 3:
            third = int(str(code)[-5:-4])
    if operation == 8:
        if content[getValue(content, position + 1, first)] == content[getValue(content, position + 2, second)]:
            content[getValue(content, position + 3, third)] = 1
        else:
            content[getValue(content, position + 3, third)] = 0
        new_position = position + 4
    elif operation == 7:
        if content[getValue(content, position + 1, first)] < content[getValue(content, position + 2, second)]:
            content[getValue(content, position + 3, third)] = 1
        else:
            content[getValue(content, position + 3, third)] = 0
        new_position = position + 4
    elif operation == 6:
        if content[getValue(content, position + 1, first)] == 0:
            new_position = content[getValue(content, position + 2, second)]
        else:
            new_position = position + 3
    elif operation == 5:
        if content[getValue(content, position + 1, first)] != 0:
            new_position = content[getValue(content, position + 2, second)]
        else:
            new_position = position + 3
    elif operation == 4:
        new_position = position + 2
        print("OutputCode: ", content[getValue(content, position + 1, first)], position, code, getValue(content, position + 1, first))
    elif operation == 3:
        new_position = position + 2
        print("Input number:")
        content[content[position + 1]] = int(raw_input())
    elif operation == 2:
        new_position = position + 4
        content[getValue(content, position + 3, third)] = content[getValue(content, position + 1, first)] * \
                                                          content[getValue(content, position + 2, second)]
    elif operation == 1:
        content[getValue(content, position + 3, third)] = content[getValue(content, position + 1, first)] + \
                                                          content[getValue(content, position + 2, second)]
        new_position = position + 4

    if operation == 99:
        new_position = len(content)
    return content, new_position


with open('file.in') as f:
    content = f.readlines()
content = [int(x) for x in content[0].split(",")]
position = 0
original = content[:]
print("Part 1")
for each in content:
    content, position = processOpCode(content, position)
    if position == len(content):
        break
position = 0
print("Part 2")
for each in original:
    original, position = processOpCode(original, position)
    if position >= len(original) - 3:
        break
