from math import sqrt
import numpy as np

def calc_distance(point_1: np.ndarray, point_2: np.ndarray):
    """
    Calculates the Euclidian distance between two points.
    """
    x_diff = point_2[0] - point_1[0]
    y_diff = point_2[1] - point_1[1]

    return sqrt(x_diff**2 + y_diff**2)

def calculate_test_point(test_point: tuple[int, int], pichu: np.ndarray, pikachu: np.ndarray):
    """
    Calculate distance between one test point and all other points, and return a sorted list.
    """
    distances = []
    for point in pikachu:
        distances.append((calc_distance(test_point, point), "Pikachu")) #append tuple with each distance between current test point and pikachu point and species

    for point in pichu:
        distances.append((calc_distance(test_point, point), "Pichu"))

    distances.sort()

    return distances

def request_testpoint():
    """
    Gets test point coordinates from user.
    """
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

def knn(k: int, distances: list):
    """
    Calculates K nearest neighbours based on a list of distances.
    """
    nearest_neighbours = distances[:k]

    pokemons = [x[1] for x in nearest_neighbours]
    majority = max(pokemons, key=pokemons.count)

    return majority

def calculate_accuracy(pikachu_train: np.ndarray[float], pikachu_test: np.ndarray[float], pichu_train: np.ndarray[float], pichu_test: np.ndarray[float]):
    """
    Calculate accuracy using train and test points.\n
    Formula: accuracy = (TP + TN) / Total
    """
    Tp = 0
    Fn = 0
    Fp = 0
    Tn = 0

    tot = len(pikachu_test) + len(pichu_test)

    for point in pikachu_test:
        distances = calculate_test_point(point, pichu_train, pikachu_train)
        species = knn(5, distances)
        if (species == "Pikachu"):
            Tp+=1
        else:
            Fn+=1

    for point in pichu_test:
        distances = calculate_test_point(point, pichu_train, pikachu_train)
        species = knn(5, distances)
        if (species == "Pichu"):
            Tn+=1
        else:
            Fp+=1

    return ((Tp + Tn)/tot)