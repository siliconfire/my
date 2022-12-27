import random

# Set up the board
board_width = 10
board_height = 10
board = [[' ' for _ in range(board_width)] for _ in range(board_height)]

# Set up the snake
snake_positions = [(1, 1), (1, 2), (1, 3)]
for x, y in snake_positions:
    board[y][x] = 'S'

# Set up the apple
apple_position = (random.randint(0, board_width - 1), random.randint(0, board_height - 1))
board[apple_position[1]][apple_position[0]] = 'A'

# Set up the direction variables
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

direction = RIGHT

# Set up the game loop
while True:
    # Print the board
    for row in board:
        print(' '.join(row))

    # Get user input
    move = input("Enter move (W/A/S/D): ")
    if move.upper() == "W":
        direction = UP
    elif move.upper() == "S":
        direction = DOWN
    elif move.upper() == "A":
        direction = LEFT
    elif move.upper() == "D":
        direction = RIGHT

    # Move the snake
    snake_positions.insert(0, (snake_positions[0][0] + direction[0], snake_positions[0][1] + direction[1]))
    if snake_positions[0] == apple_position:
        apple_position = (random.randint(0, board_width - 1), random.randint(0, board_height - 1))
        board[apple_position[1]][apple_position[0]] = 'A'
    else:
        x, y = snake_positions.pop()
        board[y][x] = ' '

    # Check for collisions
    if snake_positions[0] in snake_positions[1:]:
        print("You lost!")
        break

    if snake_positions[0][0] < 0 or snake_positions[0][0] >= board_width or snake_positions[0][1] < 0 or snake_positions[0][1] >= board_height:
        print("You lost!")
        break

    # Update the board
    x, y = snake_positions[0]
    board[y][x] = 'S'