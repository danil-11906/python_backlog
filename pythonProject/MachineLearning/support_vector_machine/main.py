import matplotlib.pyplot as plt
import random
from point import Point
from group import Group


points = []
for i in range(0, 20):
    points.append(Point(random.randint(20, 50),
                        random.randint(0, 35)))
group1 = Group(points, (random.random(), random.random(), random.random()))

points = []
for i in range(0, 30):
    points.append(Point(random.randint(0, 40),
                        random.randint(50, 70)))
group2 = Group(points, (random.random(), random.random(), random.random()))

points = []
for i in range(0, 30):
    points.append(Point(random.randint(60, 90),
                        random.randint(45, 90)))
group3 = Group(points, (random.random(), random.random(), random.random()))

group1.show()
group2.show()
group3.show()

Group.mark_two_closest_points_between_groups(group1, group2)
Group.build_line(group1, group2)
group1.unmark_all()
group2.unmark_all()

Group.mark_two_closest_points_between_groups(group1, group3)
Group.build_line(group1, group3)
group1.unmark_all()
group3.unmark_all()

Group.mark_two_closest_points_between_groups(group2, group3)
Group.build_line(group2, group3)

plt.xlim(-25, 125)
plt.ylim(-25, 125)

plt.show()
