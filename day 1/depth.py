count = 0
vals = [0,0]

with open("input.txt", "r") as f:
    for line in f:
        if (int(vals[0]) < int(line)): count += 1
        vals[0] = line 

print(count-1)