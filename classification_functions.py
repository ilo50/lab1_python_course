from math import sqrt

def calc_distance(point_1, point_2): #refactored to take coordinate pairs rather than separate x/y values
    x_diff = point_2[0] - point_1[0]
    y_diff = point_2[1] - point_1[1]

    return sqrt(x_diff**2 + y_diff**2)

###############################################################################
# classify one test point 
###############################################################################
def calculate_test_point(test_point, pichu, pikachu): # calculate distance between one test point and all other points, and return sorted

    distances = []
    for point in pikachu:
        distances.append((calc_distance(test_point, point), "Pikachu")) #append tuple with each distance between current test point and pikachu point and species

    for point in pichu:
        distances.append((calc_distance(test_point, point), "Pichu"))

    distances.sort()

    return distances

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

###############################################################################
# k nearest neighboors
###############################################################################
def knn(k, distances):
    nearest_neighbours = distances[:k]

    pokemons = [x[1] for x in nearest_neighbours]
    majority = max(pokemons, key=pokemons.count)

    return majority

###############################################################################
# calculate accuracy using train and test points
###############################################################################
def calculate_accuracy(pikachu_train, pikachu_test, pichu_train, pichu_test): #Formula: accuracy = (TP + TN) / Total
    Tp = 0
    Fn = 0
    Fp = 0
    Tn = 0

    tot = len(pikachu_test) + len(pichu_test)
    print(pikachu_test)

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

    return (f"{((Tp + Tn)/tot)*100}%")
