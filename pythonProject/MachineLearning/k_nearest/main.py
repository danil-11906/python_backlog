import matplotlib.pyplot as plt
import json
import random
import math
from point import Point
from k_nearest_classification import KNearestClassification


file_handle = open('input.json', 'r')
data = json.load(file_handle)
points = []
current_class_number = 0

for c in data:
    for point in c:
        points.append(Point(point[0], point[1], current_class_number))
    plt.text(c[0][0], c[0][1], str(current_class_number))
    current_class_number += 1

classes_count = current_class_number
colors = []
while current_class_number != 0:

    red = float(current_class_number) / float(classes_count)
    green = 1.0 - red
    blue = green

    colors.append((red, green, blue))
    current_class_number -= 1

for point in points:
    plt.scatter(point.x, point.y, c=(colors[point.class_number]))

point = Point(60, 40)
plt.scatter(point.x, point.y, c='r')

class_number = KNearestClassification(points).determine_class_number(point, int(math.ceil(math.sqrt(len(points)))), debug=True)

print(class_number)

plt.text(point.x, point.y, str(class_number))

plt.xlim(-25, 125)
plt.ylim(-25, 125)

plt.show()





