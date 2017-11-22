import ast
import math
import random
import time
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({},{})".format(self.x, self.y)

    def __str__(self):
        return "{},{}".format(self.x, self.y)


def distance(point1: Point, point2: Point):
    return math.hypot(point1.x - point2.x, point1.y - point2.y)


def efficient_closest_pair(P: list, Q: list):
    length = len(P)
    if length <= 3:
        return brute_force(P, Q)

    # Copying of arrays
    Pl = P[:length //2]
    Ql = sorted(Pl, key=lambda x: x.y)

    Pr = P[length//2:]  # O(n)
    Qr = sorted(Pr, key=lambda x: x.y)

    dl = efficient_closest_pair(Pl, Ql)
    dr = efficient_closest_pair(Pr, Qr)
    d = min(dl, dr)

    m = P[length//2].x

    S = [x for x in Q if abs(x.x - m) < d]
    num = len(S)
    dminsq = math.pow(d, 2)
    for i in range(num - 1):
        k = i + 1
        while k <= num - 1 and math.pow(S[k].y - S[i].y, 2) < dminsq:
            dminsq = min(math.pow(distance(S[k], S[i]), 2), dminsq)
            k += 1

    return math.sqrt(dminsq)


def brute_force(P: list, Q: list):
    """Time efficiency: n*n"""
    minimum = math.inf
    for point in P:
        for point2 in P:
            if point is not point2:
                minimum = min(distance(point, point2), minimum)
    return minimum


def effRec(P, Q):
    now = time.perf_counter()
    ans = efficient_closest_pair(P, Q)
    dur = time.perf_counter() - now
    print("Recursive algorithm of size {} took {} seconds.\n The minimum distance is {}".format(len(points), dur, ans))
    return dur


def effBF(P, Q):
    now = time.perf_counter()
    ans = brute_force(P, Q)
    dur = time.perf_counter() - now
    print(
        "Brute Force algorithm of size {} took {} seconds.\n The minimum distance is {}".format(len(points), dur, ans))
    return dur


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        points = ast.literal_eval(f.read())

    points = [Point(x[0], x[1]) for x in points]

    P = sorted(points, key=lambda x: x.x)
    Q = sorted(points, key=lambda x: x.y)

    effRec(P, Q)
    effBF(P, Q)
