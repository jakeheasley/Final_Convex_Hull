from Point import Point


# Function that solves and returns the convex hull
def solve_hull(point_lst):
    convex_hull = []
    for p1 in point_lst:

        # Ensures that p1 won't compare with itself
        for p2 in point_lst[0:point_lst.index(p1)] + point_lst[point_lst.index(p1) + 1:]:

            if check_points(p1, p2, point_lst):
                convex_hull.append(p1)
                convex_hull.append(p2)

    return list(set(convex_hull))


# Function that takes two points and then compares a line created
# by the points with the rest of the Point list. Returns true if
# all points are on one side of line
def check_points(p1, p2, test_lst):
    # Ensures that removing elements from test_lst won't remove
    # elements from point_lst in solve_hull
    test_lst = list(test_lst)

    # Ensures that p1 and p2 won't compare with themselves
    test_lst.remove(p1)
    test_lst.remove(p2)

    # Initial test
    p3 = test_lst[0]

    # This function will return a negative number if on one side of line
    # and a positive on the other side
    side = (p3.x - p1.x) * (p2.y - p1.y) - (p3.y - p1.y) * (p2.x - p1.x)

    for p3 in test_lst[1:]:
        new_side = (p3.x - p1.x) * (p2.y - p1.y) - (p3.y - p1.y) * (p2.x - p1.x)
        if new_side * side < 0:
            return False
    return True


def main():
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

    # Ensures that there won't be duplicates in hull
    hull = solve_hull(lst)

    hull.sort(key=lambda p: p.x, reverse=False)
    for point in hull:
        point.print_point()


if __name__ == "__main__":
    main()
