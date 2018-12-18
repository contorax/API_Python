from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    dx = p2.x - p1.x #dx = x2 - x1
    dy = p2.y - p1.y #dy = y2 - y1

    return sqrt(dx * dx + dy * dy)


print (  distance(Point (0,0), Point (3,4)))
