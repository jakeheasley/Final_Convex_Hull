"""Generates a given number of randomized points for testing"""
from Point import Point
import random


class PointGenerator:
    def __init__(self, num_points):
        self.num_points = num_points

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




