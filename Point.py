"""Point class that creates the Point object.
Contains x,y coordinates and helper functions"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Helper function that prints the x,y coordinates of a point
    def print_point(self):
        print "%d,%d" % (self.x, self.y)

    # Helper function that returns string of point
    def get_point(self):
        return "%d,%d" % (self.x, self.y)

    # Function that returns the point
    def __getitem__(self, item):
        return item
