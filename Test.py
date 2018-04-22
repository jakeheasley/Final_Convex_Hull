from Point_Generator import PointGenerator
from Convex_Hull_QH import solve_quickhull
from Convex_Hull_BF import solve_hull
from Convex_Hull_DC import solve_hull_dc
import time


p_gen = PointGenerator(0)
lst = []
avg = 0

filename = "results.txt"
f = open(filename, 'w')
for num in range(10, 101, 10):
    p_gen.set_num_points(num)
    p_gen.gen_points()
    lst = p_gen.get_points()

    for bf in range(0, 10):
        start = time.time()
        solve_hull(lst)
        final_time = time.time()-start
        avg += final_time
    avg /= 10
    f.write("BF,%d,%f\n" % (num, avg))

    avg = 0

    for DC in range(0, 10):
        start = time.time()
        solve_hull_dc(lst)
        final_time = time.time()-start
        avg += final_time
    avg /= 10
    f.write("DC,%d,%f\n" % (num, avg))

    avg = 0
    for qh in range(0, 10):
        start = time.time()
        solve_quickhull(lst)
        final_time = time.time()-start
        avg += final_time
    avg /= 10
    f.write("QH,%d,%f\n\n" % (num, avg))
