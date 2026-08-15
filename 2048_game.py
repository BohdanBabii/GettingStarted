import random


def initialize_board(board: list[list], weights: list, nums: list) -> list[list]:
    num_elements = max(5, random.randrange(0, 8))
    print(f"Number of elements to place: {num_elements}")
    free_spots = [i for i in range(16)]
    for _ in range(num_elements):
        element = random.choice(free_spots)
        board[element // 4][element % 4] = random.choices(nums, weights).pop()
        num_elements -= 1
        free_spots.remove(element)
    return board


def make_move(
    direction: str, board: list[list], weights: list, nums: list
) -> tuple[bool, list[list], list, list]:
    import copy
    board_old = copy.deepcopy(board)

    if direction == "a":
        for i in range(len(board)):
            l, r = 0, 1
            while r < len(board):
                l_element, r_element = board[i][l], board[i][r]

                if l_element == r_element and l_element != 0:
                    board[i][l] += r_element
                    board[i][r] = 0
                    l += 1
                    r += 1
                elif l_element == 0 and r_element != 0:
                    board[i][l] = r_element
                    board[i][r] = 0
                    r += 1
                elif l_element != 0 and r_element != 0 and l == r-1:
                    l += 1
                    r += 1
                elif l_element != 0 and r_element != 0:
                    l += 1
                else:
                    r += 1

    if direction == "d":
        for i in range(len(board)):
            l, r = len(board) - 2, len(board) - 1
            while l >= 0:
                l_element, r_element = board[i][l], board[i][r]

                if l_element == r_element and l_element != 0:
                    board[i][r] += l_element
                    board[i][l] = 0
                    r -= 1
                    l -= 1
                elif r_element == 0 and l_element != 0:
                    board[i][r] = l_element
                    board[i][l] = 0
                    l -= 1
                elif l_element != 0 and r_element != 0 and l == r-1:
                    l -= 1
                    r -= 1
                elif l_element != 0 and r_element != 0:
                    r -= 1
                else:
                    l -= 1

    if direction == "w":
        for i in range(len(board)):
            l, r = 0, 1
            while r < len(board):
                l_element, r_element = board[l][i], board[r][i]
                if l_element == r_element and l_element != 0:
                    board[l][i] += r_element
                    board[r][i] = 0
                    l += 1
                    r += 1
                elif l_element == 0 and r_element != 0:
                    board[l][i] = r_element
                    board[r][i] = 0
                    r += 1
                elif l_element != 0 and r_element != 0 and l == r-1:
                    l += 1
                    r += 1
                elif l_element != 0 and r_element != 0:
                    l += 1
                else:
                    r += 1

    if direction == "s":
        for i in range(len(board)):
            l, r = len(board) - 2, len(board) - 1
            while l >= 0:
                l_element, r_element = board[l][i], board[r][i]
                if l_element == r_element and l_element != 0:
                    board[r][i] += l_element
                    board[l][i] = 0
                    r -= 1
                    l -= 1
                elif r_element == 0 and l_element != 0:
                    board[r][i] = l_element
                    board[l][i] = 0
                    l -= 1
                elif l_element != 0 and r_element != 0 and l == r-1:
                    l -= 1
                    r -= 1
                elif l_element !=0 and r_element !=0:
                    r -= 1
                else:
                    l -= 1

    max_element_new = 0
    for row in board:
        max_element_new = max(max_element_new, max(row))

    max_element_seen = 0
    for row in board_old:
        max_element_seen = max(max_element_seen, max(row))

    if max_element_new > max_element_seen:
        nums.append(max_element_new)
        weights.append((1-sum(weights))/2)

    changed_board = False
    for i in range(len(board)):
        for j in range(len(board)):
            if board_old[i][j] != board[i][j]:
                changed_board = True
    return changed_board, board, weights, nums


def verify_state(board: list[list]) -> bool:
    for i in range(len(board)):
        for j in range(len(board)):
            if i - 1 >= 0:
                if board[i - 1][j] == board[i][j]:
                    return True
            if j - 1 >= 0:
                if board[i][j - 1] == board[i][j]:
                    return True
            if i + 1 < len(board):
                if board[i + 1][j] == board[i][j]:
                    return True
            if j + 1 < len(board):
                if board[i][j + 1] == board[i][j]:
                    return True
            if board[i][j] == 0:
                return True
    print("Game Over")
    return False


def add_number(board: list[list], weights: list, nums: list) -> list[list]:
    seen = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                seen.append((i, j))
    posX, posY = random.choice(seen)
    value = random.choices(nums, weights).pop()
    board[posX][posY] = value
    return board


def print_board(board: list[list]) -> None:
    print("------------------------")
    for i in range(len(board)):
        print(
            f"|{board[i][0]:<4}| {board[i][1]:<4}| {board[i][2]:<4}| {board[i][3]:<4}|"
        )
        print("------------------------")


weights: list = [0.8]
nums: list = [2]

empty_board: list[list] = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

vertical_board: list[list] = [
    [2, 0, 0, 0],
    [2, 0, 0, 0],
    [2, 0, 0, 0],
    [2, 0, 0, 0],
]

horizontal_board: list[list] = [
    [2, 2, 2, 2],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

board1: list[list] = [
    [4, 2, 2, 4],
    [4, 2, 2, 4],
    [4, 2, 2, 4],
    [4, 2, 2, 4],
]

board2: list[list] = [
    [4, 4, 4, 4],
    [2, 2, 2, 2],
    [2, 2, 2, 2],
    [4, 4, 4, 4],
]


game_over_board: list[list] = [
    [2, 4, 8, 16],
    [32, 64, 128, 256],
    [512, 1024, 2048, 4096],
    [8192, 16384, 32768, 65536],
]

broken_board: list[list] = [
    [64, 32, 8, 16],
    [2, 16, 2, 64],
    [32, 4, 16, 32],
    [16, 2, 8, 4],
]

board = initialize_board(board=empty_board, weights=weights, nums=nums)
print_board(board=board)

while True:
    direction = input("Which Direction: ")
    changed_board, board, weights, nums = make_move(
        direction=direction, 
        board=board,         
        weights=weights,
        nums=nums,
    )
    print()
    if changed_board:
        add_number(
            board=board,
            weights=weights, 
            nums=nums,
            )
    print_board(board=board)
    print(f"Weights: {weights}")
    print(f"Nums:    {nums}")
    if direction == "e" or not verify_state(board=board):
        break
