from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared

def mds(points: list[Point]):
    ...
    # sort the points by their x coordinates
    points.sort(key = lambda point: point.x)
    mid = len(points) // 2
    left, right = points[:mid], points[mid:]
    # determine middle line
    middle_line = (right[0].x + left[-1].x) / 2
    
    def recursive(points, min_distance):
        if len(points) <= 1:
            return min_distance
            # there is no distance if there is only one point or fewer
        if len(points) == 2:
            return min(min_distance, distance_squared(points[0], points[1]))
        # split the list into two halves
        mid = len(points) // 2
        left, right = points[:mid], points[mid:]
        # determine middle line
        l, r = left[-1], right[0]
        # find mininum distance of each half -> d1, d2
        d1, d2 = recursive(left, min_distance), recursive(right, min_distance)
        # find minimum between the two halves -> d
        d = min(d1,d2)
        return d
    
    d = recursive(points, float("inf"))
    # find points whose x-distance from middle line is <= d
    middle_points = []
    for p in points:
        if distance_squared(p, Point(middle_line, p.y)) <= d:
            middle_points.append(p)
    # sort those points by their y coordinate
    middle_points.sort(key= lambda p: p.y)
    # compute distance of each point to the others and keep minimum -> d_prime
    # return min of d and d_prime
    d_prime = recursive(middle_points, d)

    return min(d,d_prime)

if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))
