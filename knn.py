from typing import Tuple, List
import math


def compute_distance(point1: Tuple, point2: Tuple) -> float:
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def sort_points_by_distance(points_with_distances: List[Tuple]) -> List[Tuple]:
    return sorted(points_with_distances, key=lambda x: x[1])


def knn(source_p: Tuple, points: List, k: int) -> List[Tuple]:
    points_with_distances = [(dest_p, compute_distance(source_p, dest_p)) for dest_p in points]
    points_with_distances = sort_points_by_distance(points_with_distances)

    return points_with_distances[:k]


if __name__ == "__main__":
    points = points = [
        (1.5, 3.2),
        (4.1, 7.6),
        (9.3, 2.8),
        (5.5, 8.0),
        (6.7, 1.9),
        (2.4, 4.4),
        (8.9, 7.2),
        (3.3, 5.5),
        (7.7, 6.3),
        (0.6, 9.1)
    ]

    p = (2.1, 3.8)

    k = 3

    neighbors = knn(p, points, k=k)
    print(f"{k} nearest neighbors: {neighbors}")
