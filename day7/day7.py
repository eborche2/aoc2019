from itertools import permutations

def getValue(content, position, type):
    if type == 1:
        return position
    return content[position]


def processOpCode(content, position, _amplifier, _signal, _amp_input):
    code = abs(content[position])
    operation = code
    first = 0
    second = 0
    third = 0
    new_position = 0
    _found = False
    _end = False
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
        _signal = content[getValue(content, position + 1, first)]
        _found = True
    elif operation == 3:
        new_position = position + 2
        if not _amp_input:
            content[content[position + 1]] = _amplifier
            _amp_input = True
        else:
            content[content[position + 1]] = _signal
    elif operation == 2:
        new_position = position + 4
        content[getValue(content, position + 3, third)] = content[getValue(content, position + 1, first)] * \
                                                          content[getValue(content, position + 2, second)]
    elif operation == 1:
        content[getValue(content, position + 3, third)] = content[getValue(content, position + 1, first)] + \
                                                          content[getValue(content, position + 2, second)]
        new_position = position + 4

    if operation == 99:
        _end = True
    return content, new_position, _signal, _found, _amp_input, _end


with open('file.in') as f:
    content = f.readlines()
content = [int(x) for x in content[0].split(",")]
signal = 0
position = 0
original = content[:]
largest = 0
amplifier_order = list(permutations(range(0, 5)))
feedback_order = list(permutations(range(5, 10)))
first_content = [original[:], original[:], original[:], original[:], original[:]]
for each in amplifier_order:
    for i, amplifier in enumerate(each):
        amp_input = False
        for instructions in content:
            content, position, signal, found, amp_input, ignore = processOpCode(content, position, amplifier, signal, amp_input)
            if found:
                position = 0
                content = original[:]
                break
    if signal > largest:
        largest = signal
    signal = 0
print(largest) #part 1
largest = 0
position = 0
for z, feedback in enumerate(feedback_order):
    end = False
    amp_input = [False, False, False, False, False]
    position = [0, 0, 0, 0, 0]
    while not end:
        for i, amplifier in enumerate(feedback):
            for instructions in first_content[i]:
                first_content[i], position[i], signal, found, amp_input[i], end = processOpCode(first_content[i], position[i], amplifier,
                                                                                        signal, amp_input[i])
                if found or end:
                    if i != 4:
                        end = False
                    break
    if signal > largest:
        largest = signal
    signal = 0
    first_content = [original[:], original[:], original[:], original[:], original[:]]
print(largest)  # part 2
