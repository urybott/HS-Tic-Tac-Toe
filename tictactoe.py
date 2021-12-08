line_0 = "---------"
ps = "|"
nl = "\n"
mask_0 = "XO_"
mask_x = ['X', 'X', 'X']
mask_o = ["O"] * 3
# print(mask_x)
# print(mask_o)

msg_ = [""] * 15
msg_[0] = "Enter cells:"
msg_[1] = "Please enter 9 symbols"
msg_[2] = "Please enter 'X' or '_' or 'O' symbols only"
msg_[3] = "Enter the coordinates:"
msg_[4] = "You should enter numbers!"
msg_[5] = "Coordinates should be from 1 to 3!"
msg_[6] = "This cell is occupied! Choose another one!"
# msg_[0] = ""

cells = "_" * 9
player = "X"
finish = False
grid = []
for i in range(3):
    grid.append(["_"] * 3)
    # grid[i] = ["_"] * 3

# grid[0][2] = "O"
# grid[1][1] = "X"
# a = ""
# a_is_right = False
# while not a_is_right:
#     print(msg_[0])
#     a = input().upper()
#     c = 0
#     if len(a) == 9:
#         for s in mask_0:
#             c += a.count(s)
#         if c == 9:
#             a_is_right = True
#    else:
#        continue

# cells = a  # list(a)  #


def print_tab(x):
    for i in x:
        print(i)

def print_grid():
    result = line_0 + nl
    for i in range(3):
        result += ps + " "
        result += " ".join(grid[i]) + " "
        result += ps + nl
    result += line_0
    print(result)

def grid_count(x):
    c = 0
    for el in grid:
        c += el.count(x)
    return c
print_grid()

while not finish:

    # print("cells", cells)
    # print("grid", len(grid), grid)
    # print("lines+", len(lines)); print_tab(lines)
    # print("lines", len(lines)); print(lines)


    a_is_right = False
    a = []
    while not a_is_right:
        print(msg_[3])
        a = input().split()
        if len(a) != 2:
            print(msg_[4])
            continue
        elif not a[0].isdigit() or not a[1].isdigit():
            print(msg_[4])
            continue
        else:
            a[0] = int(a[0])
            a[1] = int(a[1])
            if 1 > a[0] or a[0] > 3 or 1 > a[1] or a[1] > 3:
                print(msg_[5])
                continue
            elif grid[a[0] - 1][a[1] - 1] != "_":
                print(msg_[6])
                continue
            else:
                a_is_right = True
                grid[a[0] - 1][a[1] - 1] = player


    print_grid()

    lines = grid.copy()
    for i in range(3):
        lines.append(["_"] * 3)

    for i in range(3):
        g = []
        for k in range(3):
            lines[i + 3][k] = grid[k][i]
    lines.append([grid[0][0], grid[1][1], grid[2][2]])  # append
    lines.append([grid[2][0], grid[1][1], grid[0][2]])

# if False:
    x_wins = 0
    o_wins = 0
    x_count = grid_count("X")  # grid.count("X")
    o_count = grid_count("O")
    s_count = grid_count("_")
    # print("x_count, o_count, s_count", x_count, o_count, s_count)
    # impossible = False
    impossible = abs(x_count - o_count) > 1

    for i in lines:
        # print(i, i == mask_x, i == mask_o, "|", i in mask_x, i in mask_o)
        if i == mask_x:
            x_wins += 1
        elif i == mask_o:
            o_wins += 1
    if x_wins > 1 or o_wins > 1 or x_wins + o_wins > 1:
        impossible = True
    if impossible:
        print("Impossible")
        break
    elif x_wins == 1:
        print("X wins")
        break
    elif o_wins == 1:
        print("O wins")
        break
    elif s_count == 0:
        print("Draw")
        break
    #else:
    #    print("Game not finished")

    if player == "X":
        player = "O"
    else:
        player = "X"
