import itertools
import math

n = int(raw_input())
wm = []
for _ in xrange(n):
    x, y = map(int, raw_input().split())
    wm.append((x, y))


def dist_euclid(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def dist_manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


equal_distance = 0
for w1, w2 in itertools.combinations(wm, 2):
    x1, y1 = w1
    x2, y2 = w2
    if x1 != x2 and y1 != y2:
        continue
    if dist_manhattan(x1, y1, x2, y2) == dist_euclid(x1, y1, x2, y2):
        equal_distance += 1

print equal_distance
