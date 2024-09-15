import pygame
import time
import random

pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display settings
dis = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
dis_width, dis_height = pygame.display.get_surface().get_size()
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
snake_block = 20  # Increased size for better visibility
snake_speed = 15

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

background_image = pygame.image.load('background.jpg')
background_image = pygame.transform.scale(background_image, (dis_width, dis_height))

def score(score):
    value = score_font.render("Score: " + str(score), True, black)
    dis.blit(value, [10, 10])

def high_score(score):
    value = score_font.render("High Score: " + str(score), True, black)
    dis.blit(value, [dis_width / 2, 10])

def our_snake(snake_block, snake_list):
    for segment in snake_list:
        pygame.draw.rect(dis, green, [segment[0], segment[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

    high_score_value = 0

    while not game_over:

        while game_close:
            dis.blit(background_image, (0, 0))
            message("You Lost! Press Q-Quit or C-Play Again", red)
            score(Length_of_snake - 1)
            high_score(high_score_value)
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
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.blit(background_image, (0, 0))
        pygame.draw.rect(dis, black, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for segment in snake_List[:-1]:
            if segment == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        score(Length_of_snake - 1)
        high_score(high_score_value)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            Length_of_snake += 1
            if Length_of_snake - 1 > high_score_value:
                high_score_value = Length_of_snake - 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
