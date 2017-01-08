from functools import wraps
import time


def timer(func, precision: int=4):
    @wraps(func)
    def wrapper(*args, **kwargs):
        c1, p1 = time.clock(), time.perf_counter()
        var = func(*args, **kwargs)
        c2, p2 = time.clock() - c1, time.perf_counter() - p1
        print(" Function '{}' ran in {:.{p}f} s. ({:.{p}f} s. CPU only)".format(func.__name__, p2, c2,
                                                                                p=precision))
        return var
    return wrapper
