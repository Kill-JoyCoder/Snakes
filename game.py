import pygame
import time
import random

# Initialize Pygame
pygame.init()


white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
grey = (97, 97, 97)
green = (0, 255, 0)
blue = (8, 110, 168)

display_width = 800
display_height = 600

block_size = 20
snake_speed = 15

font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    gameDisplay.blit(mesg, [display_width / 6, display_height / 3])


def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(gameDisplay, green, [x[0], x[1], block_size, block_size])


# Function to display the game
def gameLoop():
    game_over = False
    game_close = False

    # Initialize snake position and movement
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0

    snake_list = []
    snake_length = 1

    # Initialize position of food
    rand_food_x = round(random.randrange(0, display_width - block_size) / block_size) * block_size
    rand_food_y = round(random.randrange(0, display_height - block_size) / block_size) * block_size

    while not game_over:

        while game_close:
            gameDisplay.fill(black)
            message("Press C to play again, Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            game_close = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, red, [rand_food_x, rand_food_y, block_size, block_size])

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(block_size, snake_list)

        pygame.display.update()

        if lead_x == rand_food_x and lead_y == rand_food_y:
            rand_food_x = round(random.randrange(0, display_width - block_size) / block_size) * block_size
            rand_food_y = round(random.randrange(0, display_height - block_size) / block_size) * block_size
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


# Set display dimensions and create the game window
gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)
pygame.display.set_caption('Snakes!')

clock = pygame.time.Clock()

# Start the game
gameLoop()
