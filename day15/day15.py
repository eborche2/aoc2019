from copy import deepcopy
from random import randint


class repair():
    position = 0
    base = 0
    end = False
    spot = (0, 0)
    last = [(0, 0)]
    dead_end = []
    locations = {spot: 'S'}
    oxygen = None


    def __init__(self):
        self.run_program()

    def getValue(self, content, position, type, base):
        if type == 2:
            return base + content[position]
        if type == 1:
            return position
        return content[position]

    def processOpCode(self):
        code = abs(self.content[self.position])
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
                self.base += self.content[self.getValue(self.content, self.position + 1, first, self.base)]
                new_position = self.position + 2
            elif operation == 8:
                if self.content[self.getValue(self.content, self.position + 1, first, self.base)] == self.content[self.getValue(self.content, self.position + 2, second, self.base)]:
                    self.content[self.getValue(self.content, self.position + 3, third, self.base)] = 1
                else:
                    self.content[self.getValue(self.content, self.position + 3, third, self.base)] = 0
                new_position = self.position + 4
            elif operation == 7:
                if self.content[self.getValue(self.content, self.position + 1, first, self.base)] < self.content[self.getValue(self.content, self.position + 2, second, self.base)]:
                    self.content[self.getValue(self.content, self.position + 3, third, self.base)] = 1
                else:
                    self.content[self.getValue(self.content, self.position + 3, third, self.base)] = 0
                new_position = self.position + 4
            elif operation == 6:
                if self.content[self.getValue(self.content, self.position + 1, first, self.base)] == 0:
                    new_position = self.content[self.getValue(self.content, self.position + 2, second, self.base)]
                else:
                    new_position = self.position + 3
            elif operation == 5:
                if self.content[self.getValue(self.content, self.position + 1, first, self.base)] != 0:
                    new_position = self.content[self.getValue(self.content, self.position + 2, second, self.base)]
                else:
                    new_position = self.position + 3
            elif operation == 4:
                new_position = self.position + 2
                result = self.content[self.getValue(self.content, self.position + 1, first, self.base)]
                if result == 0:
                    self.locations[self.spot] = '#'
                    self.spot = deepcopy(self.last[-1])
                if result == 1:
                    if self.spot != (0, 0):
                        self.locations[self.spot] = ' '
                if result == 2:
                    self.locations[self.spot] = 'O'
                    self.oxygen = len(self.last)
                self.display()
            elif operation == 3:
                new_position = self.position + 2
                self.display()
                direction = self.determineNextDirection()
                if direction == -1:
                    _end = True
                    direction = 1
                self.content[self.getValue(self.content, self.position + 1, first, self.base)] = direction
            elif operation == 2:
                new_position = self.position + 4
                self.content[self.getValue(self.content, self.position + 3, third, self.base)] = self.content[self.getValue(self.content, self.position + 1, first, self.base)] * \
                                                                  self.content[self.getValue(self.content, self.position + 2, second, self.base)]
            elif operation == 1:
                self.content[self.getValue(self.content, self.position + 3, third, self.base)] = self.content[self.getValue(self.content, self.position + 1, first, self.base)] + \
                                                                  self.content[self.getValue(self.content, self.position + 2, second, self.base)]
                new_position = self.position + 4

            if operation == 99:
                _end = True
            self.position = new_position
        except IndexError:
            self.content += [0] * 4000
            return _end
        return _end

    def display(self):
        smallestx = 0
        smallesty = 0
        greatestx = 0
        greatesty = 0
        for key, _ in self.locations.iteritems():
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
                if (x, y) in self.locations:
                    add_row = add_row[:-1]
                    add_row += self.locations[(x, y)]
            rows.append(add_row)
        rows.reverse()
        print("Display")
        for each in rows:
            print(each)

    def determineNextDirection(self):
        can_go = []
        options = [4, 3, 1, 2]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        locs = []
        for i, check in enumerate(dirs):
            direction = (check[0] + self.spot[0], check[1] + self.spot[1])
            locs.append(direction)
            if direction not in self.locations or self.locations[direction] != '#' and direction not in self.dead_end:
                can_go.append(i)
        if len(can_go) == 0:
            return -1
        if len(can_go) == 1:
            self.dead_end.append(deepcopy(self.spot))
            nex = 0
        else:
            nex = randint(0, len(can_go))
        self.last.append(deepcopy(self.spot))
        self.spot = locs[can_go[nex]]
        return options[can_go[nex]]

    def count_steps(self):
        last_oxy = deepcopy(self.last[0: self.oxygen])
        last_oxy.pop(0)
        unfixed = True
        while unfixed:
            for i, x in enumerate(last_oxy):
                if i != len(last_oxy) - 1 - last_oxy[::-1].index(x):
                    last_oxy = last_oxy[0: i] + last_oxy[len(last_oxy) - 1 - last_oxy[::-1].index(x): ]
                    break
                if i == len(last_oxy) - 1:
                    unfixed = False
        return last_oxy

    def map_size(self):
        mapping = [self.last[self.oxygen]]
        count = 0
        while len(mapping) > 0:
            new_mapping = []
            count += 1
            for each in mapping:
                self.locations[each] = 'o'
                for check in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    spot = (each[0] + check[0], each[1] + check[1])
                    if spot in self.locations:
                        if self.locations[spot] in [' ', 'S']:
                            new_mapping.append(spot)
            self.display()
            mapping = new_mapping
        self.display()
        print(count - 1)

    def run_program(self):
        with open('file.in') as f:
            content = f.readlines()
        self.content = [int(x) for x in content[0].split(",")]
        while not self.end:
            self.end = self.processOpCode()
        print(len(self.count_steps()))
        self.map_size()


repair()
