import sys
import pygame
from food import Food
from snake import Snake

SCREEN_SIZE = (1000, 600)
SCREEN_BACK_COLOR = (240, 240, 240)
SCREEN_CAPTION = "A Snake"
HEAD_COLOR = (238, 107, 39)
BODY_COLOR = (111, 227, 146)
FOOD_COLOR = (44, 36, 84)
FOOD_RIDUS = 3
HEAD_RIDUS = 5
HEAD_MOVE_STEP = 5
BORN_POSX = 300
BORN_POSY = 150
BORN_LENGTH = 4


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(SCREEN_CAPTION)
    screen.fill(SCREEN_BACK_COLOR)

    snake = Snake(BORN_POSX, BORN_POSY, BORN_LENGTH, SCREEN_SIZE[0], SCREEN_SIZE[1])
    food = Food(SCREEN_SIZE[0], SCREEN_SIZE[1], snake)

    while True:
        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                sys.exit()

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_UP:
                    snake.set_up()
                if ev.key == pygame.K_DOWN:
                    snake.set_down()
                if ev.key == pygame.K_LEFT:
                    snake.set_left()
                if ev.key == pygame.K_RIGHT:
                    snake.set_right()

            if ev.type == pygame.KEYUP:
                if ev.key == pygame.K_UP:
                    snake.reset_up()
                if ev.key == pygame.K_DOWN:
                    snake.reset_down()
                if ev.key == pygame.K_LEFT:
                    snake.reset_left()
                if ev.key == pygame.K_RIGHT:
                    snake.reset_right()

        # pygame.time.delay(5)
        snake.move(HEAD_MOVE_STEP)
        if food.is_eaten():
            del(food)
            food = Food(SCREEN_SIZE[0], SCREEN_SIZE[1], snake)
            snake.grow()


        screen.fill(SCREEN_BACK_COLOR)

        # foods
        pygame.draw.circle(screen, FOOD_COLOR, (food.posx, food.posy), FOOD_RIDUS)

        # snake
        for i in range(1, len(snake.body)):
            pygame.draw.circle(screen, BODY_COLOR, (snake.body[i][0], snake.body[i][1]), HEAD_RIDUS)
        pygame.draw.circle(screen, HEAD_COLOR, (snake.body[0][0], snake.body[0][1]), HEAD_RIDUS)

        pygame.display.flip()


if __name__ == "__main__":
    main()
