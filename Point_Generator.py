"""Object that generates a given number of random points"""
from Point import Point
import random


class PointGenerator:
    def __init__(self):
        self.num_points = 0

    def __init__(self, num_points):
        self.num_points = num_points

    # Generates num_points random points within a plane
    # of num_points^2 x num_points^2
    def gen_points(self):
        filename = 'Points.txt'
        point_range = pow(self.num_points,2)

        x_list = random.sample(range(0, point_range), self.num_points)
        y_list = random.sample(range(0, point_range), self.num_points)

        lst = []
        for x, y in zip(x_list, y_list):
            lst.append(Point(x, y))

        f = open(filename, 'w')
        for point in lst:
            f.write(point.get_point())
            f.write("\n")

    # Returns a list of points
    def get_points(self):
        lst = []

        # Reads points from file 'Points.txt' into program.
        # Coordinates are designated with commas
        lines = open("Points.txt").read().splitlines()
        for line in lines:

            # If there is a blank line at end of Points.txt
            if not line:
                continue
            x, y = line.split(",")
            lst.append(Point(int(x), int(y)))
        return lst

    # Sets new number of points
    def set_num_points(self, points):
        self.num_points = points




