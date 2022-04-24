from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def deplacer(self, *args):
        self.x += args[0]
        self.y += args[1]

    def distance(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def afficher(self):
        print("x = ", self.x)
        print("y = ", self.y)

    def __str__(self):
        return ("x = " + str(self.x) + "\ny = " + str(self.y))

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
