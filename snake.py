import pygame
import time
import random

pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
PASTEL_GREEN = (144, 238, 144)  # Soft pastel green color
SNAKE_COLOR = (0, 128, 0)  # Dark green for the snake
FOOD_COLOR = (255, 69, 0)  # Red-orange for the food

# Display settings
DIS_WIDTH = 800
DIS_HEIGHT = 600
DIS = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption('Snake Game')

CLOCK = pygame.time.Clock()
SNAKE_BLOCK = 20
SNAKE_SPEED = 15

FONT_STYLE = pygame.font.SysFont(None, 50)
SCORE_FONT = pygame.font.SysFont(None, 35)

# Initialize high score
high_score_value = 0

def draw_score(score, high_score):
    value = SCORE_FONT.render(f"Score: {score}", True, BLACK)
    DIS.blit(value, [10, 10])
    value = SCORE_FONT.render(f"High Score: {high_score}", True, BLACK)
    DIS.blit(value, [DIS_WIDTH - 200, 10])

def draw_snake(snake_block, snake_list):
    for segment in snake_list:
        pygame.draw.circle(DIS, SNAKE_COLOR, (segment[0] + SNAKE_BLOCK // 2, segment[1] + SNAKE_BLOCK // 2), SNAKE_BLOCK // 2)

def draw_message(msg, color):
    mesg = FONT_STYLE.render(msg, True, color)
    DIS.blit(mesg, [DIS_WIDTH / 6, DIS_HEIGHT / 3])

def draw_background():
    for y in range(0, DIS_HEIGHT, 10):
        pygame.draw.line(DIS, PASTEL_GREEN, (0, y), (DIS_WIDTH, y), 10)

def gameLoop():
    global high_score_value  # Access the global high score variable

    game_over = False
    game_close = False

    x1 = DIS_WIDTH / 2
    y1 = DIS_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
    foody = round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK

    current_score = 0

    while not game_over:

        while game_close:
            draw_background()
            draw_message("You Lost! Press Q-Quit or C-Play Again", RED)
            draw_score(current_score, high_score_value)
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
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        draw_background()
        pygame.draw.rect(DIS, FOOD_COLOR, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for segment in snake_List[:-1]:
            if segment == snake_Head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_List)
        current_score = Length_of_snake - 1
        if current_score > high_score_value:
            high_score_value = current_score
        draw_score(current_score, high_score_value)

        pygame.display.update()

        # Check for collision with food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
            foody = round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
            Length_of_snake += 1

        CLOCK.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

if __name__ == "__main__":
    gameLoop()
