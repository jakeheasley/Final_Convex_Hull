# Tests how long it takes to solve a convex hull of various
# sizes for Divide and Conquer, Brute Force, and Quickhull algorithms
from Point_Generator import PointGenerator
from Convex_Hull_QH import solve_quickhull
from Convex_Hull_BF import solve_hull
from Convex_Hull_DC import solve_hull_dc
import time


# Creating a point generator to randomly generate points
p_gen = PointGenerator(0)
lst = []
avg = 0

# Creating a file to write results to
filename = "results.txt"
f = open(filename, 'w')
# For loop that goes from 10 to 100, steps of 10
for num in range(10, 101, 10):

    # Generating num points
    p_gen.set_num_points(num)
    p_gen.gen_points()
    lst = p_gen.get_points()

    # Runs algorithm 10 times and then finds average time
    for bf in range(0, 10):
        start = time.time()
        solve_hull(lst)
        final_time = time.time()-start
        avg += final_time
    avg /= 10

    # Writes the algorithm, number of points, and avg time spent to results.txt
    f.write("BF,%d,%f\n" % (num, avg))

    avg = 0

    # Runs algorithm 10 times for Divide and Conquer
    for DC in range(0, 10):
        start = time.time()
        solve_hull_dc(lst)
        final_time = time.time()-start
        avg += final_time
    avg /= 10
    f.write("DC,%d,%f\n" % (num, avg))

    avg = 0

    # Runs algorithm 10 times for Quickhull
    for qh in range(0, 10):
        start = time.time()
        solve_quickhull(lst)
        final_time = time.time()-start
        avg += final_time
    avg /= 10
    f.write("QH,%d,%f\n\n" % (num, avg))

# For loop that goes from 200 to 500, steps of 100
for num in range(200, 501, 100):

    # Generating num random points
    p_gen.set_num_points(num)
    p_gen.gen_points()
    lst = p_gen.get_points()

    for bf2 in range(0, 10):
        start = time.time()
        solve_hull(lst)
        final_time = time.time()-start
        avg += final_time
    avg /= 10
    f.write("BF,%d,%f\n" % (num, avg))

    avg = 0

    for DC2 in range(0, 10):
        start = time.time()
        solve_hull_dc(lst)
        final_time = time.time()-start
        avg += final_time
    avg /= 10
    f.write("DC,%d,%f\n" % (num, avg))

    avg = 0
    for qh2 in range(0, 10):
        start = time.time()
        solve_quickhull(lst)
        final_time = time.time()-start
        avg += final_time
    avg /= 10
    f.write("QH,%d,%f\n\n" % (num, avg))