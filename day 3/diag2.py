diag_data = []

with open("input.txt", "r") as f:
    for line in f:
        diag_data.append(line.strip())

def filter_data_by_position(input_data, position, filter_value):
    output_data = []
    for line in input_data:
        if line[position] != str(filter_value):
            continue
        output_data.append(line)
    return output_data

def count_abundant_in_position(input_data, position, reverse_count=False):
    position_vals = []
    for line in input_data:
        position_vals.append(line[position])
    if reverse_count:
        if position_vals.count("1") < position_vals.count("0"):
            return 1
        else: return 0
    if position_vals.count("0") > position_vals.count("1"):
        return 0
    else: return 1

search_data = {
    "iteration" : 0,
    "data" : diag_data
}

oxygen_generator_val = ""
co2_scrubber_val = ""

# Oxygen generator
for _ in diag_data[0]:
    if len(search_data["data"]) == 1: break
    search_data["data"] = filter_data_by_position(search_data["data"], search_data["iteration"], count_abundant_in_position(search_data["data"], search_data["iteration"], reverse_count=False)) # This is disgusting
    search_data["iteration"] += 1

oxygen_generator_val = search_data["data"][0]

search_data["data"] = diag_data
search_data["iteration"] = 0

### CO2 generator
for _ in diag_data[0]:
    if len(search_data["data"]) == 1: break
    search_data["data"] = filter_data_by_position(search_data["data"], search_data["iteration"], count_abundant_in_position(search_data["data"], search_data["iteration"], reverse_count=True)) # This is also disgusting
    search_data["iteration"] += 1

co2_scrubber_val = search_data["data"][0]

print("Oxygen generator value in binary: {}".format(oxygen_generator_val))
print("Oxygen generator value in decimal: {}".format(int(("0b" + oxygen_generator_val), 2)))
print("CO2 scrubber value in binary: {}".format(co2_scrubber_val))
print("CO2 scrubber value in decimal: {}".format(int(("0b" + co2_scrubber_val), 2)))
print("Values multiplied together: {}".format(int(("0b" + oxygen_generator_val), 2)*int(("0b" + co2_scrubber_val), 2)))