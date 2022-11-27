import matplotlib.pyplot as plt
from shortest_unclosed_path import ShortestUnclosedPath
from point import Point


points = [Point(0, 0) for i in range(0, 120)]
# [p.gen_coordinates(0, 100) for p in points]

for i in range(0, 120):
    points[i].gen_coordinates(0, 40, 0, 40)

for i in range(20, 50):
    points[i].gen_coordinates(0, 40, 60, 100)

for i in range(50, 80):
    points[i].gen_coordinates(60, 100, 0, 40)

for i in range(80, 120):
    points[i].gen_coordinates(60, 100, 60, 100)

ShortestUnclosedPath(points).split_into_clusters(4)

plt.style.use('seaborn-whitegrid')
plt.xlim(-25, 125)
plt.ylim(-25, 125)

plt.show()
