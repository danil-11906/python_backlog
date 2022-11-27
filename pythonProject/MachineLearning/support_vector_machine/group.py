import sys
import matplotlib.pyplot as plt
import numpy as np


class Group:

    def __init__(self, points, color):
        self.points = points
        self.marked_points = []
        self.color = color

    def unmark_all(self):
        self.marked_points = []

    def show(self):
        plt.scatter(
            [point.x for point in self.points],
            [point.y for point in self.points],
            c=self.color
        )

    @staticmethod
    def mark_two_closest_points_between_groups(group1, group2):
        Group.mark_closest_points_between_groups(group1, group2)
        Group.mark_closest_points_between_groups(group1, group2)

    @staticmethod
    def mark_closest_points_between_groups(group1, group2):

        nearest_distance = sys.maxsize
        nearest_p1 = None
        nearest_p2 = None

        for p1 in group1.points:
            for p2 in group2.points:
                distance = p1.calculate_distance_to_point(p2)
                if distance < nearest_distance:
                    if p1 not in group1.marked_points and p2 not in group2.marked_points:
                        nearest_distance = distance
                        nearest_p1 = p1
                        nearest_p2 = p2

        plt.plot([nearest_p1.x, nearest_p2.x],
                 [nearest_p1.y, nearest_p2.y],
                 c='g')

        group1.marked_points.append(nearest_p1)
        group2.marked_points.append(nearest_p2)

    @staticmethod
    def build_line(group1, group2):
        x = np.arange(-20, 120, .5)

        x0 = (group2.marked_points[0].x + group1.marked_points[0].x) / 2
        y0 = (group2.marked_points[0].y + group1.marked_points[0].y) / 2
        x1 = (group2.marked_points[1].x + group1.marked_points[1].x) / 2
        y1 = (group2.marked_points[1].y + group1.marked_points[1].y) / 2

        # print(group2.marked_points[0].x, group1.marked_points[0].x)
        # print(x0)
        # print(group2.marked_points[0].y, group1.marked_points[0].y)
        # print(y0)
        # print(group2.marked_points[1].x, group1.marked_points[1].x)
        # print(x1)
        # print(group2.marked_points[1].y, group1.marked_points[1].y)
        # print(y1)
        # print('\n\n')

        if x1 - x0 == 0:
            x1 += 1

        plt.plot(x, ((x - x0) * (y1 - y0)) / (x1 - x0) + y0, c='r')

