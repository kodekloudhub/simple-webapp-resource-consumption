from multiprocessing import Pool
from multiprocessing import cpu_count


def f(x):
    while True:
        x*x

processes = cpu_count()
print('utilizing %d cores\n' % processes)
pool = Pool(processes)
pool.map(f, [0, 1])