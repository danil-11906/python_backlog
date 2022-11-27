from point import Point
from math import sin
from math import cos
from math import pi
import matplotlib.pyplot as plt
import sys


class Cluster:
    points = []

    def __init__(self, points):
        self.points = points

    def calculate_center(self):
        if len(self.points) == 0:
            return Point(0, 0)

        x_coordinates_sum = 0
        y_coordinates_sum = 0

        for p in self.points:
            x_coordinates_sum += p.x
            y_coordinates_sum += p.y

        center = Point(x_coordinates_sum / len(self.points),
                       y_coordinates_sum / len(self.points))

        return center

    def get_furthest_point(self, point):
        max_distance = 0
        furthest_point = self.points[0]
        for p in self.points:
            distance = p.calculate_distance_to_point(point)
            if distance > max_distance:
                max_distance = distance
                furthest_point = p
        return furthest_point

    def add_equidistant_points_around_center(self, count, debug=False):
        points = []
        center = self.calculate_center()

        if debug:
            plt.scatter(center.x, center.y, c='red')

        radius = center.calculate_distance_to_point(self.get_furthest_point(center))

        for i in range(0, count):
            points.append(Point(radius * sin(((i * 2 * pi) / count) + pi / 4) + center.x,
                                radius * cos(((i * 2 * pi) / count) + pi / 4) + center.y))

        if debug:
            plt.scatter([p.x for p in points], [p.y for p in points], c='red')

        return points

    def split_into_clusters_around_points(self, points):
        clusters = []
        for i in range(0, len(points)):
            clusters.append(Cluster([]))

        for p in self.points:
            min_distance_to_point = 999999
            min_distance_point_index = 0
            for i in range(0, len(points)):
                distance = p.calculate_distance_to_point(points[i])
                if distance < min_distance_to_point:
                    min_distance_to_point = distance
                    min_distance_point_index = i
            clusters[min_distance_point_index].points.append(p)

        return clusters
