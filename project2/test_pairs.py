import pytest
from .project2 import *


@pytest.mark.parametrize("points", [

    [(0, 0), (7, 6), (2, 20), (12, 5), (16, 16), (5, 8), (19, 7), (14, 22), (8, 19), (7, 29), (10, 11),
     (1, 13)],
    [(0, 1), (99, 50), (153, 22), (44, 11)],
    [(23, 294), (755, 430), (751, 487), (574, 451), (321, 745), (65, 55), (813, 299), (409, 749), (204, 396),
     (917, 848), (777, 515)]

])
def test_pairs(points):
    print(points)
    points = [Point(x[0], x[1]) for x in points]
    P = sorted(points, key=lambda x: x.x)
    Q = sorted(points, key=lambda x: x.y)
    assert brute_force(P, Q) == efficient_closest_pair(P, Q)



def test_random():
    sam = [[x, y] for x in range(1001) for y in range(1001)]
    for i in range(10, 1000):
        points = random.sample(sam, i)
        points = [Point(x[0], x[1]) for x in points]
        P = sorted(points, key=lambda x: x.x)
        Q = sorted(points, key=lambda x: x.y)
        assert brute_force(P, Q) == efficient_closest_pair(P, Q)
