from math import sqrt

def calc_distance(x1, y1, x2, y2):
    x_diff = x2 - x1
    y_diff = y2 - y1

    return sqrt(x_diff**2 + y_diff**2)

def clean_data(data):
    x = []
    y = []

    data = [line[1:-2] for line in data] #slice so ( ) \n gets removed

    for coordinate in data:
        x_coord, y_coord = coordinate.split(", ")
        x.append(float(x_coord))
        y.append(float(y_coord))

    return x, y

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()[1:-1] #read file but skip header