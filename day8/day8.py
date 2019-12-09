

with open('file.in') as f:
    content = f.readlines()[0]

layers = [[]]
count = 0
layer = 0
for pixel in content:
    if count > 149:
        layer += 1
        count = 0
        layers.append([])
    layers[layer].append(int(pixel))
    count += 1
lowest = (150, 0)

for i, each in enumerate(layers):
    if lowest[0] > each.count(0) > 0:
        lowest = (each.count(0), i)
print(layers[lowest[1]].count(1) * layers[lowest[1]].count(2)) # part 1
layer1 = layers[0]
for x in range(1, len(layers)):
    for i, pixel in enumerate(layer1):
        if pixel == 2:
            layer1[i] = layers[x][i]
for i, pixel in enumerate(layer1):
    if pixel == 0:
        layer1[i] = ' '# hard to see if this is printed
    else:
        layer1[i] = 'W'
s = ""
print(s.join(layer1[0:25]))
print(s.join(layer1[25:50]))
print(s.join(layer1[50:75]))
print(s.join(layer1[75:100]))
print(s.join(layer1[100:125]))
print(s.join(layer1[125:150]))#Part 2

