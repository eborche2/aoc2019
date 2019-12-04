
start = 372304
end = 847060
candidates1 = 0
candidates2 = 0
for number in range(start, end + 1):
    first = False
    second = False
    good = False
    number = str(number)
    last = 'not'
    for i, num in enumerate(number):
        if i == 5:
            if second:
                good = True
            break
        if number[i + 1] == num:
            first = True
            if second:
                if last == num:
                    second = False
            elif last != num:
                second = True
                last = num
        else:
            last = 'not'
            if second:
                good = True
            second = False
        if int(num) > int(number[i + 1]):
            first = False
            good = False
            break
    if first:
        candidates1 += 1
    if good:
        candidates2 += 1
print(candidates1) #part 1
print(candidates2) #part 2
