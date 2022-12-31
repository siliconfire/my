import pygame
import random

# Set up the pygame window
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake")

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the snake
snake_positions = [(100, 100), (80, 100), (60, 100)]
snake_body = pygame.Surface((20, 20))
snake_body.fill(WHITE)

# Set up the apple
apple_position = (random.randint(0, 29) * 20, random.randint(0, 29) * 20)
apple = pygame.Surface((20, 20))
apple.fill("RED")

# Set up the direction variables
UP = (0, -20)
DOWN = (0, 20)
LEFT = (-20, 0)
RIGHT = (20, 0)

direction = RIGHT

# Set up the clock
clock = pygame.time.Clock()

# Set up the game loop
while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Check for key presses
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        direction = UP
    if pressed[pygame.K_DOWN]:
        direction = DOWN
    if pressed[pygame.K_LEFT]:
        direction = LEFT
    if pressed[pygame.K_RIGHT]:
        direction = RIGHT

    # Move the snake
    snake_positions.insert(0, (snake_positions[0][0] + direction[0], snake_positions[0][1] + direction[1]))
    if snake_positions[0] == apple_position:
        apple_position = (random.randint(0, 29) * 20, random.randint(0, 29) * 20)
    else:
        snake_positions.pop()

    # Check for collisions
    if snake_positions[0] in snake_positions[1:]:
        print("You lost!")
        break

    if snake_positions[0][0] < 0 or snake_positions[0][0] > 580 or snake_positions[0][1] < 0 or snake_positions[0][1] > 580:
        print("You lost!")
        break

    # Draw the screen
    screen.fill((0, 0, 0))
    screen.blit(apple, apple_position)
    for position in snake_positions:
        screen.blit(snake_body, position)
    pygame.display.update()
