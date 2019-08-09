from direction import Direction


class Snake():

    def __init__(self, headx, heady, length, screenedgex, screenedgey):
        self.headx = headx
        self.heady = heady
        self.edgex = screenedgex
        self.edgey = screenedgey
        self.up = Direction.none
        self.down = Direction.none
        self.left = Direction.none
        self.right = Direction.none
        self.body = []

        for i in range(0, length):
            self.body.append([headx, heady])

    def move(self, step):
        if (self.up != Direction.none or self.down != Direction.none or
                self.left != Direction.none or self.right != Direction.none):

            if self.up == Direction.up:
                if (self.heady - step >= 0):
                    self.heady -= step
            if self.down == Direction.down:
                if (self.heady + step <= self.edgey):
                    self.heady += step
            if self.left == Direction.left:
                if (self.headx - step >= 0):
                    self.headx -= step
            if self.right == Direction.right:
                if (self.headx + step <= self.edgex):
                    self.headx += step

            index = len(self.body) - 1
            while (index >= 0):
                self.body[index][0] = self.body[index - 1][0]
                self.body[index][1] = self.body[index - 1][1]
                index -= 1

            self.body[0][0] = self.headx
            self.body[0][1] = self.heady

        # print(self.body)

    def set_up(self):
        if self.down != Direction.down:
            self.up = Direction.up

    def set_down(self):
        if self.up != Direction.up:
            self.down = Direction.down

    def set_left(self):
        if self.right != Direction.right:
            self.left = Direction.left

    def set_right(self):
        if self.left != Direction.left:
            self.right = Direction.right

    def reset_up(self):
        self.up = Direction.none

    def reset_down(self):
        self.down = Direction.none

    def reset_left(self):
        self.left = Direction.none

    def reset_right(self):
        self.right = Direction.none
