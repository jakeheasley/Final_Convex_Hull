from Point import Point


def solve_hull(point_arr):
    convex_hull = []
    for p1 in point_arr:
        for p2 in point_arr[0:point_arr.index(p1)] + point_arr[point_arr.index(p1)+1:]:

            if check_points(p1, p2, point_arr):
                convex_hull.append(p1)
                convex_hull.append(p2)

    return convex_hull


def check_points(p1, p2, test_arr):
    test_arr = list(test_arr)
    test_arr.remove(p1)
    test_arr.remove(p2)

    p3 = test_arr[0]
    side = (p3.x-p1.x)*(p2.y-p1.y)-(p3.y-p1.y)*(p2.x-p1.x)

    for p3 in test_arr[1:]:
        new_side = (p3.x-p1.x)*(p2.y-p1.y)-(p3.y-p1.y)*(p2.x-p1.x)
        if new_side*side < 0:
            return False
    return True


arr = []
lines = open("Points.txt").read().splitlines()
for line in lines:
    x, y = line.split(",")
    arr.append(Point(int(x), int(y)))

hull = list(set(solve_hull(arr)))
hull.sort(key=lambda p: p.x, reverse=False)
for point in hull:
    point.print_point()

