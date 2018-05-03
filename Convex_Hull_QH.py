from Point import Point


# Function that finds the minimum and maximum x points in a list.
def get_min_max(point_lst):
    # Ensures that min_x can always be updated to
    # correspond with the lowest x value in the list.
    min_x = float('inf')
    min_y = 0
    max_x = 0
    max_y = 0

    for i in point_lst:
        if i.x < min_x:
            min_x = i.x
            min_y = i.y
        if i.x > max_x:
            max_x = i.x
            max_y = i.y

    min_point = Point(int(min_x), int(min_y))
    max_point = Point(int(max_x), int(max_y))

    return min_point, max_point


# Function that compares a line created by two points with the
# the rest of the Point list. It then returns a list that contains
# all the points that lie on the left side of this line.
def get_left_points(p1, p2, point_lst):
    # Ensures that removing elements from test_lst won't remove
    # elements from point_lst in solve_hull
    test_lst = list(point_lst)
    left_lst = []

    for point in test_lst[0:]:
        # This function will return a negative number if point is on one side of
        # the line and a positive number if on the other side
        side = (p2.x - p1.x) * (point.y - p1.y) - (p2.y - p1.y) * (point.x - p1.x)
        if side > 0:
            left_lst.append(point)

    return left_lst


# Function that determines and returns the distance from a point to
# a line created by two other points.
def distance(p1, p2, point):
    nominator = abs((p2.y - p1.y) * point.x - (p2.x - p1.x) * point.y + p2.x * p1.y - p2.y * p1.x)
    denominator = ((p2.y - p1.y)**2 + (p2.x - p1.x) ** 2) ** 0.5

    result = nominator / denominator
    return result


# Function that determines and returns the point farthest away
# from a line created by two other points.
def get_max_point_from_line(p1, p2, point_lst):
    max_distance = 0

    max_point = []

    for point in point_lst:
        # Ensures that p1 and p2 won't compare with themselves
        if point != p1 and point != p2:
            distance_from_line = distance(p1, p2, point)
            if distance_from_line > max_distance:
                max_distance = distance_from_line
                max_point = point

    return max_point


# Function that solves and returns the quickhull
def solve_quickhull(point_lst):
    lst_min, lst_max = get_min_max(point_lst)

    convex_hull = quickhull(lst_min, lst_max, point_lst)

    convex_hull = convex_hull + quickhull(lst_max, lst_min, point_lst)

    return convex_hull


def quickhull(lst_min, lst_max, point_lst):

    left_points = get_left_points(lst_min, lst_max, point_lst)

    pointC = get_max_point_from_line(lst_min, lst_max, left_points)

    # Ensures that the recursive function ends when there are no
    # more points to compare
    if len(left_points) < 1:
        return [lst_max]

    hullpoints = quickhull(lst_min, pointC, left_points)
    hullpoints = hullpoints + quickhull(pointC, lst_max,left_points)

    return hullpoints


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
    hull = list(set(solve_quickhull(lst)))

    hull.sort(key=lambda p: p.x, reverse=False)
    for point in hull:
        point.print_point()


if __name__ == "__main__":
    main()
