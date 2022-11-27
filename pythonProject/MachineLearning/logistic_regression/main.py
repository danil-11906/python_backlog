import matplotlib.pyplot as plt
import json
from logistic_regression import LogisticRegression
from point import P2

file_handle = open('input.json', 'r')
data = json.load(file_handle)
points = []
current_class_number = 0

for c in data:
    for point in c:
        points.append(P2(point[0], point[1], current_class_number))
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

log_reg = LogisticRegression(points)
log_reg.calculate(debug=True)

for p in points:
    probability_class_1 = log_reg.p(p, 1)

    print("P " + str(p) + " = " + str(probability_class_1))
    if probability_class_1 > 0.5:
        p.class_number = 1
    else:
        p.class_number = 0

for point in points:
    plt.scatter(point.x, point.y, c=(colors[point.class_number]))

plt.xlim(-0.25, 1.25)
plt.ylim(-0.25, 1.25)

plt.show()
