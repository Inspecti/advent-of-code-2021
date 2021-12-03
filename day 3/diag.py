diag_data = []

with open("input.txt", "r") as f:
    for line in f:
        diag_data.append(line.strip())

position_vals = {}

for pos, _ in enumerate(diag_data[0]):
    for line in diag_data:
        try:
            position_vals[str(pos)].append(line[pos])
        except KeyError:
            position_vals[str(pos)] = [line[pos]]

gamma_rate = ""
epsilon_rate = ""

for key in position_vals.keys():
    if ("".join(position_vals[key])).count('0') < ("".join(position_vals[key])).count('1'):
        gamma_rate += "1"
        epsilon_rate += "0"
    else: 
        gamma_rate += "0"
        epsilon_rate += "1"

print("Gamma rate in binary:   " + gamma_rate)
print("Epsilon rate in binary: " + epsilon_rate)
print("Multiplied together in decimal: {}".format(int(("0b"+gamma_rate), 2) * int(("0b"+epsilon_rate), 2)))