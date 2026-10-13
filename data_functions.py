import re # used by read_test_points
import numpy as np

def read_data_points(file_path: str):
    """
    Opens a file of coordinates and returns an array of tuple coordinates.
    """
    with open(file_path, "r") as file:
        data =  file.readlines()[1:] #skip first row

        x = []
        y = []
        
        data = [line[1:-2] for line in data] #slice so ( ) \n gets removed
        
        for coordinate in data:
            x_coord, y_coord = coordinate.split(", ")
            x.append(float(x_coord))
            y.append(float(y_coord))
        
        data_points = np.array(list(zip(x, y)))

        return data_points

def read_test_points(file_path: str):
    """
    Reads a single-row file of test point tuples and returns an NDArray.
    """
    with open(file_path, "r") as file:
        test_points = file.readlines()[0] 

        matches = re.findall(r'[\d]{1,}', test_points) # find all digits with atleast length 1

        test_x = []
        test_y = []

        while matches: # alternate between x and y, y is at end of list, pop first
            test_x.append(float(matches.pop(0))) #changed to pop(0) and reversed x/y order to keep
            test_y.append(float(matches.pop(0))) #the initial coordinate order

    test_points = np.array(list(zip(test_x, test_y)))

    return test_points

def split_data(data: np.ndarray):
    """
    Shuffles and splits data into two NDArrays of the first five points and the remaining points.
    """
    np.random.shuffle(data) # randomize all data

    test, train = np.split(data, [5]) #split at index 5 into two variables
    return(train, test)