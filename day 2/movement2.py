movement_data = []
horpos = 0
depth = 0
aim = 0


with open("input.txt", "r") as f:
    for line in f:
        movement_data.append(line.strip().split(" "))

for instruction in movement_data:
    if instruction[0] == "forward":
        depth += aim*int(instruction[1])
        horpos += int(instruction[1])
    elif instruction[0] == "down":
        aim += int(instruction[1])
    elif instruction[0] == "up":
        aim -= int(instruction[1])
    else: continue

print("Horizontal position: {}".format(horpos))
print("Depth: {}".format(depth))
print("Multiplied together: {}".format(horpos*depth))