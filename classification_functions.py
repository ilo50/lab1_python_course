from math import sqrt

def calc_distance(x1, y1, x2, y2):
    x_diff = x2 - x1
    y_diff = y2 - y1

    return sqrt(x_diff**2 + y_diff**2)