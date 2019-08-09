from direction import Direction

class Circle():

    def __init__(self, x, y):
        self.posx = x
        self.posy = y
        self.up = Direction.none
        self.down = Direction.none
        self.left = Direction.none
        self.right = Direction.none

    def move(self):
        if self.up == Direction.up:
            self.posy -= 4
        if self.down == Direction.down:
            self.posy += 4
        if self.left == Direction.left:
            self.posx -= 4
        if self.right == Direction.right:
            self.posx += 4

    def set_up(self):
        self.up = Direction.up

    def set_down(self):
        self.down = Direction.down

    def set_left(self):
        self.left = Direction.left

    def set_right(self):
        self.right = Direction.right

    def reset_up(self):
        self.up = Direction.none

    def reset_down(self):
        self.down = Direction.none

    def reset_left(self):
        self.left = Direction.none

    def reset_right(self):
        self.right = Direction.none
