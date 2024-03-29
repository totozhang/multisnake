import random


class Food():

    def __init__(self, screenedgex, screenedgey, snake):
        self.posx, self.posy = get_valid_position(screenedgex, screenedgey, snake)
        self.snake = snake

    def is_eaten(self):
        if int((self.snake.headx - self.posx) ** 2 + (self.snake.heady - self.posy) ** 2) < 100:
            return True
        else:
            return False


def get_valid_position(screenedgex, screenedgey, snake):
    x = random.randint(1, screenedgex)
    y = random.randint(1, screenedgey)

    while is_position_in_snake(x, y, snake):
        x = random.randint(1, screenedgex)
        y = random.randint(1, screenedgey)

    return x, y


def is_position_in_snake(x, y, snake):
    for item in snake.body:
        if (item[0] == x) and (item[1] == y):
            return True

    return False
