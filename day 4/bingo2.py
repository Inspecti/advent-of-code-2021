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
                bingo_boards["board{}".format(board_count)] = {"haswin": False, "vals": board_temp_values}
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

def check_all_boards_for_win(boards):
    for key in boards.keys():
        if boards[key]["haswin"] == False: return False
    return True
    

turn = 0
latest_winning_board = ""
latest_winining_draw = ""
all_boards_win = False

for draw in bingo_all_draws:
    turn += 1
    bingo_iter_draws.append(draw)
    if turn < 5: continue
    for key in bingo_boards.keys():
        if bingo_boards[key]["haswin"]:
            continue
        win, output, bingorow = check_board_for_win(bingo_boards[key]["vals"], bingo_iter_draws)
        if win:
            bingo_boards[key]["haswin"] = True
            latest_winining_draw = draw
            latest_winning_board = key
            if check_all_boards_for_win(bingo_boards):
                all_boards_win = True 
                break
    if all_boards_win: break

unmarked_numbers = []

if win:
    print("Found bingo at turn {}!".format(turn))
    print("Draws so far: {}".format(bingo_iter_draws))
    print("Last winning bingo board was {} with {} bingo and matching values of:".format(latest_winning_board, output))
    for row in bingo_boards[latest_winning_board]["vals"]:
        print(row)
    print("------------------")
    for line in bingo_boards[latest_winning_board]["vals"]:
        for draw in bingo_iter_draws:
            if draw in line: line.remove(draw)
        unmarked_numbers += line
    for num in unmarked_numbers:
        print(num)
    print(sum([int(x) for x in unmarked_numbers]))
    print(int(latest_winining_draw))
    print("Multiplied: {}".format((sum([int(x) for x in unmarked_numbers]))*(int(latest_winining_draw))))
else:
    print("No bingo!")