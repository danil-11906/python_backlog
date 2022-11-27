import sys
import math
from collections import Counter


class KNearestClassification:

    def __init__(self, points):
        self.points = points

    def determine_class_number(self, point, k, debug=False):

        used_nearest_points = []
        nearest_classes = []

        for _ in range(0, k):

            nearest_i = 0
            nearest_distance = sys.maxsize

            for i in range(0, len(self.points)):
                if i in used_nearest_points:
                    continue
                distance = point.calculate_distance_to_point(self.points[i])
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_i = i

            used_nearest_points.append(nearest_i)
            nearest_classes.append(self.points[nearest_i].class_number)

        if debug:
            print(nearest_classes)

        return Counter(nearest_classes).most_common()[0][0]
