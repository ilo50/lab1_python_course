from math import sqrt

def calc_distance(point_1, point_2): #refactored to take coordinate pairs rather than separate x/y values
    x_diff = point_2[0] - point_1[0]
    y_diff = point_2[1] - point_1[1]

    return sqrt(x_diff**2 + y_diff**2)

###############################################################################
# classify one test point 
###############################################################################
def classify_test_point(test_point, pichu, pikachu):

    distances = []
    for point in pikachu:
        distances.append((calc_distance(test_point, point), "Pikachu")) #append tuple with each distance between current test point and pikachu point and species

    for point in pichu:
        distances.append((calc_distance(test_point, point), "Pichu"))

    distances.sort()

    print(f"Test point: {test_point} qualified as {distances[0][1]}")

###############################################################################
# request test point from user and classify
###############################################################################
def request_testpoint():

    x = input("input x coordinate")
    y = input("input y coordinate")

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        raise ValueError("Only integer and float is allowed")
    

    if x < 0 or y < 0:
        raise ValueError("coordinate cannot contain negative values")
    
    return x, y

       