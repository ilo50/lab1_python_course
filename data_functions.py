def clean_data(data):
    x = []
    y = []

    data = [line[1:-2] for line in data] #slice so ( ) \n gets removed

    for coordinate in data:
        x_coord, y_coord = coordinate.split(", ")
        x.append(float(x_coord))
        y.append(float(y_coord))

    return x, y

def read_data_points(file_path):
    with open(file_path, "r") as file:
        return file.readlines()[1:-1] #read file but skip header

def read_test_points(file_path):
    with open(file_path, "r") as file:
        return file.readlines() #read file but skip header
