import sys
import pygame
from circle import Circle

def main():
    SCREEN_SIZE = (1000, 600)
    SCREEN_BACK_COLOR = (240, 240, 240)
    SCREEN_CAPTION = "A Moving Circle"
    CIRCLE_COLOR = (238, 107, 39)
    CIRCLE_RIDUS = 6

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(SCREEN_CAPTION)
    screen.fill(SCREEN_BACK_COLOR)

    circle = Circle(300, 150)

    while True:
        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                sys.exit()

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_UP:
                    circle.set_up()
                if ev.key == pygame.K_DOWN:
                    circle.set_down()
                if ev.key == pygame.K_LEFT:
                    circle.set_left()
                if ev.key == pygame.K_RIGHT:
                    circle.set_right()

            if ev.type == pygame.KEYUP:
                if ev.key == pygame.K_UP:
                    circle.reset_up()
                if ev.key == pygame.K_DOWN:
                    circle.reset_down()
                if ev.key == pygame.K_LEFT:
                    circle.reset_left()
                if ev.key == pygame.K_RIGHT:
                    circle.reset_right()

        pygame.time.delay(5)
        circle.move()
        screen.fill(SCREEN_BACK_COLOR)
        pygame.draw.circle(screen, CIRCLE_COLOR, (circle.posx, circle.posy), CIRCLE_RIDUS)
        pygame.display.flip()


if __name__ == "__main__":
    main()
