from cluster import Cluster
import matplotlib.pyplot as plt


class KMid:

    def __init__(self, points):
        self.cluster = Cluster(points)

    def split_into_clusters(self, count, debug=True):
        equidistant_points = self.cluster.add_equidistant_points_around_center(count, debug=debug)

        clusters = self.cluster.split_into_clusters_around_points(equidistant_points)

        centers = []

        while True:
            old_centers = centers
            centers = []
            for c in clusters:
                centers.append(c.calculate_center())

            clusters = self.cluster.split_into_clusters_around_points(centers)

            distance_is_little = True
            for j in range(0, len(old_centers)):
                if centers[j].calculate_distance_to_point(old_centers[j]) > 0:
                    distance_is_little = False

            if distance_is_little:
                break

        if debug:
            plt.scatter([p.x for p in centers], [p.y for p in centers], c='red')

        return clusters
