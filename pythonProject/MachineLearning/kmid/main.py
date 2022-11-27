import matplotlib.pyplot as plt
from point import Point
from kmid import KMid
import json
import random

points = [Point(0, 0) for i in range(0, 120)]
# [p.gen_coordinates(0, 100) for p in points]

for i in range(0, 20):
    points[i].gen_coordinates(0, 30, 0, 30)

for i in range(20, 50):
    points[i].gen_coordinates(0, 40, 50, 70)

for i in range(50, 80):
    points[i].gen_coordinates(60, 90, 0, 30)

for i in range(80, 120):
    points[i].gen_coordinates(70, 90, 70, 90)

clusters = KMid(points).split_into_clusters(4, debug=True)
cluster_number = 0
to_json = []

for i in range(0, len(clusters)):

    to_json.append([])
    points = clusters[i].points
    color = (random.random(), random.random(), random.random())

    for p in points:
        to_json[i].append([p.x, p.y])
        plt.scatter(p.x, p.y, c=color)

    cluster_number += 1

file_output = 'kmid/output.json'
file_handle = open(file_output, 'w')
file_handle.write(json.dumps(to_json))
file_handle.close()

plt.xlim(-25, 125)
plt.ylim(-25, 125)

plt.show()
