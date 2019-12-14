from copy import deepcopy
from random import randint


class breakout_game():
    position = 0
    x = 0
    y = 0
    pin = 0
    base = 0
    end, first, second = False, False, False
    locations = {}
    scores = []
    ball_positions = []
    direction = 0
    joystick = 0

    def __init__(self):
        self.run_program()

    def get_key(self, val):
        for key, value in self.locations.items():
            if val == value:
                return key
        return None

    def determine_direction(self):
        if len(self.ball_positions) > 2:
            first = self.ball_positions[-3]
            middle = self.ball_positions[-2]
            last = self.ball_positions[-1]
            if first[0] == last[0] or first[1] == last[1]:
                if (middle[0], middle[1] - 1) in self.locations:
                    if self.locations[(middle[0], middle[1] - 1)] == 'B':
                        self.locations[(middle[0], middle[1] - 1)] = ' '
                if (middle[0] - 1, middle[1] - 1) in self.locations:
                    if self.locations[(middle[0] - 1, middle[1] - 1)] == 'B':
                        self.locations[(middle[0] - 1, middle[1] - 1)] = ' '
                if (middle[0] + 1, middle[1] - 1) in self.locations:
                    if self.locations[(middle[0] + 1, middle[1] - 1)] == 'B':
                        self.locations[(middle[0] + 1, middle[1] - 1)] = ' '
                if (middle[0] - 1, middle[1]) in self.locations:
                    if self.locations[(middle[0] - 1, middle[1])] == 'B':
                        self.locations[(middle[0] - 1, middle[1])] = ' '
                if (middle[0] + 1, middle[1]) in self.locations:
                    if self.locations[(middle[0] + 1, middle[1])] == 'B':
                        self.locations[(middle[0] + 1, middle[1])] = ' '
                if ((middle[0], middle[1] + 1)) in self.locations:
                    if self.locations[(middle[0], middle[1] + 1)] == 'B':
                        self.locations[(middle[0], middle[1] + 1)] = ' '
                if (middle[0] - 1, middle[1] + 1) in self.locations:
                    if self.locations[(middle[0] - 1, middle[1] + 1)] == 'B':
                        self.locations[(middle[0] - 1, middle[1] + 1)] = ' '
                if (middle[0] + 1, middle[1] + 1) in self.locations:
                    if self.locations[(middle[0] + 1, middle[1] + 1)] == 'B':
                        self.locations[(middle[0] + 1, middle[1] + 1)] = ' '

    def determine_intersect(self):
        paddle = self.get_key('P')
        ball = self.ball_positions[-1]
        if paddle[0] < ball[0]:
            self.joystick = 1
        elif paddle[0] > ball[0]:
            self.joystick = -1
        else:
            self.joystick = 0
        return

    def breakout(self):
        if (self.x, self.y) == (-1, 0):
            self.scores.append(self.pin)
            return
        if self.pin == 0:
            return
        if self.pin == 1:
            self.locations[(self.x, self.y)] = 'W'
            return
        if self.pin == 2:
            self.locations[(self.x, self.y)] = 'B'
            return
        if self.pin == 3:
            if self.get_key('P'):
                self.locations[self.get_key('P')] = ' '
            self.locations[(self.x, self.y)] = 'P'
            return
        if self.pin == 4:
            self.ball_positions.append((self.x, self.y))
            if (self.x, self.y) in self.locations:
                if self.locations[(self.x, self.y)] not in ['B', 'A', ' ']:
                    return
            if self.get_key('A'):
                self.locations[self.get_key('A')] = ' '
            self.determine_direction()
            self.locations[(self.x, self.y)] = 'A'

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
                if self.second:
                    self.pin = self.content[self.getValue(self.content, self.position + 1, first, self.base)]
                    self.first = False
                elif self.first:
                    self.y = self.content[self.getValue(self.content, self.position + 1, first, self.base)]
                    self.second = True
                else:
                    self.x = self.content[self.getValue(self.content, self.position + 1, first, self.base)]
                    self.first = True
            elif operation == 3:
                new_position = self.position + 2
                self.determine_intersect()
                self.display()
                self.content[self.getValue(self.content, self.position + 1, first, self.base)] = self.joystick
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
        if len(self.scores) > 0 and self.content[385] != self.scores[-1]:
            self.scores.append(self.content[385])
        return _end

    def run_program(self):
        with open('file.in') as f:
            content = f.readlines()
        self.content = [int(x) for x in content[0].split(",")]
        while not self.end:
            self.end = self.processOpCode()
            if not self.first and self.second:
                self.second = False
                self.breakout()
        self.display()
        count = 0
        for each in self.locations:
            if self.locations[each] == 'B':
                count += 1
        print(count)
        print(self.scores[-2])



# Part 1 place a 1 in position 0, Part 2 place a 2 in position 0 and uncomment print statement.
# Never could quite get it to display properly.

breakout_game()
