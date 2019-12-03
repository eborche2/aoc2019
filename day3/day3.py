
intersections = []
steps = []

def mark_map(direction, count, wire_map, current_location, green_wire, start_count):
    tick = 1
    axis = 0
    if direction in ['L', 'D']:
        tick = -1
    if direction in ['U', 'D']:
        axis = 1
    for i in range(count):
        x_axis = current_location[0] if axis is 1 else current_location[0] + tick
        y_axis = current_location[1] if axis is 0 else current_location[1] + tick
        current_location = (x_axis, y_axis)
        start_count += 1
        if not green_wire:
            if current_location not in wire_map:
                wire_map[current_location] = ("red", start_count)
        else:
            if current_location in wire_map and wire_map[current_location][0] == "red":
                intersections.append(current_location)
                steps.append(wire_map[current_location][1] + start_count)
            else:
                if current_location not in wire_map:
                    wire_map[current_location] = ("green", start_count)
    return wire_map, current_location, start_count

with open('file.in') as f:
    content = f.readlines()
red = content[0].split(",")

with open('file2.in') as f:
    content = f.readlines()
green = content[0].split(",")

wire_map = {}
current_location = (0, 0)
wire_map[current_location] = "Origin"
start_count = 0
for each in red:
    wire_map, current_location, start_count = mark_map(each[:1], int(each[1:]), wire_map, current_location, False, start_count)
current_location = (0, 0)
start_count = 0
for each in green:
    wire_map, current_location, start_count = mark_map(each[:1], int(each[1:]), wire_map, current_location, True, start_count)
lowest = abs(intersections[0][0]) + abs(intersections[0][1])
pair = 0
for i, each in enumerate(intersections):
    if lowest > abs(each[0]) + abs(each[1]):
        pair = i
        lowest = abs(each[0]) + abs(each[1])
print(lowest) # Part 1
print(min(steps)) # Part 2

