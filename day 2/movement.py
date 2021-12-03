movement_data = {
    "up": [],
    "down": [],
    "forward": []
}

with open("input.txt", "r") as f:
    for line in f:
        vals = line.strip().split(" ")
        movement_data[vals[0]].append(int(vals[1]))

vertpos = sum(movement_data["down"])-sum(movement_data["up"])
horpos = sum(movement_data["forward"])

print("Vertical position: {}".format(vertpos))
print("Horizontal position: {}".format(horpos))
print("Multiplied together: {}".format(str(vertpos*horpos)))