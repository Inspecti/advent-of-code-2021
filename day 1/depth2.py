count = 0
window_vals = []

try:
    with open("input.txt", "r") as f:
        for i, line in enumerate(f):
            if i < 3: 
                window_vals.append(int(line))
                continue
            val = int(line)
            if sum(window_vals) < (sum(window_vals[-2:]) + val): count+=1
            window_vals = window_vals[-2:]
            window_vals.append(val)
    print(count)
except StopIteration:
    print("End of file")
    print(count)