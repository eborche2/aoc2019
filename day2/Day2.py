def perform_calculation(content, operation, start):
    content[int(content[start + 3])] = str(eval(content[int(content[start + 1])] + operation + content[int(content[start + 2])]))
    return content


def loop(content):
    start = 0
    while start < len(content):
        if content[start] == '99':
            start = len(content)
            continue
        if content[start] == '1':
            content = perform_calculation(content, '+', start)
        if content[start] == '2':
            content = perform_calculation(content, '*', start)
        start += 4
    return content
with open('file.in') as f:
    content = f.readlines()
content = content[0].split(",")
original = content[:]
content = loop(content)

print(content[0]) #solution 1

noun = 0
verb = 0
while noun < 100 and verb < 100:
    test = original[:]
    test[1] = str(noun)
    test[2] = str(verb)
    if noun == 99:
        if verb == 99:
            noun += 1
            verb += 1
        else:
            verb += 1
            noun = 0
    test = loop(test)
    if test[0] == '19690720':
        print(100 * noun + verb) #solution 2
        noun = 100
        verb = 100
    noun += 1
