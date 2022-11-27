from math import sqrt


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    x = 0
    y = 0

    def __str__(self):
        return str(self.x) + "," + str(self.y)

    def calculate_distance_to_point(self, point):
        return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)
