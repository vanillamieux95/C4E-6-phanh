class GameModel:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def next_pos(self, dx, dy):
        #calcul8 the next position
        return (self.x + dx, self.y + dy)

    def print(self):
        #to be able to print out the value
        print ("x = {0}, y = {1}".format(self.x, self.y))