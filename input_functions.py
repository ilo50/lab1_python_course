def request_testpoint():

    x = input("input x coordinate")
    y = input("input y coordinate")

    if not isinstance(x, (int, float)) and isinstance(y, (int, float)):
        raise TypeError("test point must be integer or float")

    if x < 0 or y < 0:
        raise ValueError("coordinate cannot contain negative values")
    
    result = NotImplemented(x, y)

    