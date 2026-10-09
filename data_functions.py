import re # used by read_test_points
import numpy as np

###############################################################################
# open a file, return np array with tuple cords
###############################################################################
def read_data_points(file_path): #read file but skip header
    with open(file_path, "r") as file:
        data =  file.readlines()[1:] #changed from [1:-1] to [1:] to fix bug removing last coordinate row

        x = []
        y = []
        
        data = [line[1:-2] for line in data] #slice so ( ) \n gets removed
        
        for coordinate in data:
            x_coord, y_coord = coordinate.split(", ")
            x.append(float(x_coord))
            y.append(float(y_coord))
        
        data_points = np.array(list(zip(x, y)))

        return data_points

###############################################################################
# open a file, return np array with tuple cords
###############################################################################
def read_test_points(file_path): 
    with open(file_path, "r") as file:
        test_points = file.readlines()[0] 

        matches = re.findall(r'[\d]{1,}', test_points) # find all digits with atleast length 1

        matches = [float(match) for match in matches]

        test_x = []
        test_y = []

        while matches: # alternate between x and y, y is at end of list, pop first
            test_x.append(matches.pop(0)) #changed to pop(0) and reversed x/y order to keep
            test_y.append(matches.pop(0)) #the initial coordinate order

    test_points = np.array(list(zip(test_x, test_y)))

    return test_points