import random
from math import sqrt


class P2:

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


class P3:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.z)

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z

        return self

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

        return self

    def __eq__(self, other):
        return self.x == other.x & self.y == other.y & self.z == other.z

    def multiply(self, multiplier):
        """
        :type multiplier: float
        """
        self.x *= multiplier
        self.y *= multiplier
        self.z *= multiplier

        return self

    def __copy__(self):
        return P3(self.x, self.y, self.z)

    def calculate_distance_to_point(self, point):
        return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2 + (self.z - point.z) ** 2)
