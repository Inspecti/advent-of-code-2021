bingo_all_draws = []
bingo_iter_draws = []
board_count = 0
bingo_boards = {
}

with open("input.txt", "r") as f:
    board_temp_values = []
    for i, line in enumerate(f):
        line = line.strip()
        if i == 0:
            bingo_all_draws += line.split(",")
            continue
        if line == "":
            if board_temp_values != []:
                board_count += 1
                bingo_boards["board{}".format(board_count)] = board_temp_values
            board_temp_values = []
        else:
            board_temp_values.append(list(filter(None, line.split(" "))))

def check_board_for_win(board, draws):
    for line in board: # check for horizontal bingo
        if all(val in draws for val in line):
            return True, "horizontal", line
    for i in range(0, len(board[0])): # checking for vertical bingo
        vertvals = []
        for line in board:
            vertvals.append(line[i])
        if all(val in draws for val in vertvals):
            return True, "vertical", vertvals
    return False, "no bingo", []

turn = 0
winning_board = ""

for draw in bingo_all_draws:
    turn += 1
    bingo_iter_draws.append(draw)
    if turn < 5: continue
    for key in bingo_boards.keys():
        win, output, bingorow = check_board_for_win(bingo_boards[key], bingo_iter_draws)
        #print("{}: {}, {}, {}".format(key, win, output, bingorow))
        if win:
            winning_board = key 
            break
    if win: break

unmarked_numbers = []

if win:
    print("Found bingo at turn {}!".format(turn))
    print("Draws so far: {}".format(bingo_iter_draws))
    print("Winning bingo board was {} with {} bingo and matching values of:".format(winning_board, output))
    for row in bingo_boards[winning_board]:
        print(row)
    print("------------------")
    for line in bingo_boards[winning_board]:
        for draw in bingo_iter_draws:
            if draw in line: line.remove(draw)
        unmarked_numbers += line
    print(sum([int(x) for x in unmarked_numbers]))
    print(int(bingo_iter_draws[-1:][0]))
    print("Multiplied: {}".format((sum([int(x) for x in unmarked_numbers]))*(int(bingo_iter_draws[-1:][0]))))
else:
    print("No bingo!")