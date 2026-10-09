from math import sqrt

def calc_distance(point_1, point_2): #refactored to take coordinate pairs rather than separate x/y values
    x_diff = point_2[0] - point_1[0]
    y_diff = point_2[1] - point_1[1]

    return sqrt(x_diff**2 + y_diff**2)