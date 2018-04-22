""" Solves the convex hull with divide and conquer methodology
Credit to MSeifert on Stackoverflow and GeeksforGeeks.com for elements of the algorithm"""
from Point import Point
from Convex_Hull_BF import solve_hull
import math
import functools


def quad(point):
    if point.x >= 0 and point.y >=0:
        return 1
    elif point.x <= 0 and point.y >= 0:
        return 2
    elif point.x <= 0 and point.y <= 0:
        return 3
    else:
        return 4


def compare(a, b):
    p1 = Point(a.x-center.x, a.y-center.y)
    p2 = Point(b.x-center.x, b.y-center.y)

    one = quad(p1)
    two = quad(p2)

    if one != two:
        return one < two
    return a.y*b.x < b.y*a.x


def clockwiseangle_and_distance(point):
    # Vector between point and the origin: v = p - o
    vector = Point(point.x-center.x, point.y-center.y)

    # Length of vector: ||v||
    lenvector = math.hypot(vector.x, vector.y)

    # If length is zero there is no angle
    if lenvector == 0:
        return -math.pi, 0

    # Normalize vector: v/||v||
    normalized = Point(vector.x/lenvector, vector.y/lenvector)
    dotprod  = normalized.x*refvec.x + normalized.y*refvec.y     # x1*x2 + y1*y2

    diffprod = refvec[1]*normalized.x - refvec.x*normalized.y     # x1*y2 - y1*x2
    angle = math.atan2(diffprod, dotprod)

    # Negative angles represent counter-clockwise angles so we need to subtract them
    # from 2*pi (360 degrees)
    if angle < 0:
        return 2*math.pi+angle, lenvector

    # I return first the angle because that's the primary sorting criterium
    # but if two vectors have the same angle then the shorter distance should come first.
    return angle, lenvector


def orientation(p1, p2, p3):
    check = (p3.x - p2.x) * (p2.y - p1.y) - (p3.y - p2.y) * (p2.x - p1.x)
    if check == 0:
        return 0
    elif check > 0:
        return 1
    else:
        return -1


def solve_hull_dc(point_list):
    length = len(point_list)

    # Return the convex hull when length is <= 5
    # bruteforce method is fast enough with fewer points to make
    # the speed difference negligible
    if length <= 5:
        return solve_hull(point_list)

    # Recursively breaking down point_list
    left_hull = solve_hull_dc(point_list[:length/2])
    right_hull = solve_hull_dc(point_list[length/2:])

    # Merges the two hulls when both have been broken down
    return merge(left_hull, right_hull)


def merge(left_hull, right_hull):
    print "\nMERGE\n\n"
    print"LEFT HULL UNSORTED"
    for point in left_hull:
        point.print_point()
    print""

    print "RIGHT HULL UNSORTED"
    for point in right_hull:
        point.print_point()
    print""

    # Global variables that are used for sorting the lists
    global refvec
    global center

    # refvec set to 0,-1 so the list is sorted counterclockwise instead of clockwise
    refvec = Point(0, -1)

    len_l = len(left_hull)
    len_r = len(right_hull)

    # Determining the center of the left hull
    center = Point(sum(p.x for p in left_hull)/len(left_hull), sum(p.y for p in left_hull)/len(left_hull))

    # Sorting left hull into counterclockwise order
    left_hull = sorted(left_hull, key=clockwiseangle_and_distance)

    # Setting center to right_hull and sorting right_hull in counterclockwise order
    center = Point(sum(p.x for p in right_hull) / len(right_hull), sum(p.y for p in right_hull) / len(right_hull))
    right_hull = sorted(right_hull, key=clockwiseangle_and_distance)

    # Setting init_l and r values to 0
    init_l = 0
    init_r = 0

    # Determining the right-most point on left_hull and left most point on right_hull
    for l in left_hull:
        if l.x > left_hull[init_l].x:
            init_l = left_hull.index(l)
    for r in right_hull:
        if r.x < right_hull[init_r].x:
            init_r = right_hull.index(r)
    print "LEFT RIGHT"
    left_hull[init_l].print_point()
    right_hull[init_r].print_point()
    print ""

    # Holder variables that maintain the original init_l and r
    og_l = init_l
    og_r = init_r

    print "LEFT HULL SORTED"
    for point in left_hull:
        point.print_point()
    print ""
    print "RIGHT HULL SORTED"
    for point in right_hull:
        point.print_point()


    print ""
    print "UPPER"
    # finding upper tangent points
    finish = False
    while not finish:
        finish = True

        print "LEFT"
        left_hull[(init_l + 1) % len_l].print_point()
        print orientation(left_hull[init_l], right_hull[init_r], left_hull[(init_l + 1) % len_l])
        # Upper left tangent point
        while orientation(left_hull[init_l], right_hull[init_r], left_hull[(init_l+1) % len_l]) <= 0:

            left_hull[(init_l+1) % len_l].print_point()
            print orientation(left_hull[init_l], right_hull[init_r], left_hull[(init_l+1) % len_l])
            init_l = (init_l+1) % len_l

        # Upper right tangent point
        while orientation(right_hull[init_r], left_hull[init_l], right_hull[(len_r + init_r - 1) % len_r]) >= 0:
            print "RIGHT"
            right_hull[(init_r + 1) % len_r].print_point()
            print orientation(right_hull[init_r], left_hull[init_l], right_hull[(len_r + init_r - 1) % len_r])
            init_r = (init_r-1) % len_r
            finish = False

    # Setting left and right upper tangent line points
    upper_l = init_l
    upper_r = init_r

    init_l = og_l
    init_r = og_r

    print ""
    print "LOWER"
    # finding lower tangent points
    finish = False
    while not finish:
        finish = True

        # Finding lower tangent point for right_hull
        while orientation(left_hull[init_l], right_hull[init_r], right_hull[(init_r + 1) % len_r]) >= 0:
            print "RIGHT"
            right_hull[(init_r + 1) % len_r].print_point()
            print orientation(left_hull[init_l], right_hull[init_r], left_hull[(init_l + 1) % len_l])
            init_r = (len_r + init_r+1) % len_r

        # Finding lower tangent point for left_hull
        while orientation(right_hull[init_r], left_hull[init_l], left_hull[(len_l + init_l - 1) % len_l]) <= 0:
            print "LEFT"
            left_hull[(len_l + init_l - 1) % len_l].print_point()
            print orientation(right_hull[init_r], left_hull[init_l], left_hull[(len_l + init_l - 1) % len_l])
            init_l = (len_l + init_l - 1) % len_l
            finish = False

    # Setting left and right lower tangent line points
    lower_l = init_l
    lower_r = init_r

    print "upper"
    left_hull[upper_l].print_point()
    right_hull[upper_r].print_point()

    print "lower"
    left_hull[lower_l].print_point()
    right_hull[lower_r].print_point()

    # Initialize the hull
    hull = []
    point = upper_l

    # Add points from lower tangent to upper tangent point in left_hull
    hull.append(left_hull[upper_l])
    while point != lower_l:
        point = (point+1) % len_l
        hull.append(left_hull[point])

    point = lower_r

    # Add points from lower tangent to upper tangent point in left_hull
    hull.append(right_hull[lower_r])
    while point != upper_r:
        point = (point + 1) % len_r
        hull.append(right_hull[point])

    print ""
    print "HULL"
    for point in hull:
        point.print_point()
    return hull


def main():
    lst = []

    # Reads points from file 'Points.txt' into program.
    # Coordinates are designated with commas
    lines = open("Points.txt").read().splitlines()
    for line in lines:
        x, y = line.split(",")
        lst.append(Point(int(x), int(y)))

    # Ensures that there won't be duplicates in hull
    lst.sort(key=lambda p: p.x, reverse=False)
    hull = list(set(solve_hull_dc(lst)))

    print ""
    hull.sort(key=lambda p: p.x, reverse=False)
    for point in hull:
        point.print_point()


if __name__ == "__main__":
    main()
