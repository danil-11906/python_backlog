import random
from math import sqrt


class Point:

    def __init__(self, x, y, class_number=0):
        self.x = x
        self.y = y
        self.class_number = class_number

    def __str__(self):
        return str(self.x) + " " + str(self.y)

    def gen_coordinates(self, min_x, max_x, min_y, max_y):
        self.x = random.randint(min_x, max_x)
        self.y = random.randint(min_y, max_y)

    def calculate_distance_to_point(self, point):
        return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)
