import time

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        #print((method.__name__, args, kw, te-ts))
        print('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000), "\n")
        return result

    return timed


from ctypes import *
from python_bubl_sort import obj

@timeit
def call_small_py():
    obj.small_arr_sorting()
    return

@timeit
def call_small_go():
    lib = cdll.LoadLibrary('./golang_bubl_sort.so')
    lib.small_arr_sorting()

@timeit
def call_big_py():
    obj.big_arr_sorting(10000)
    return

@timeit
def call_big_go():
    lib = cdll.LoadLibrary('./golang_bubl_sort.so')
    lib.big_arr_sorting.argtypes = [c_longlong]
    lib.big_arr_sorting.restype = None
    lib.big_arr_sorting(10000)


call_small_py()
call_small_go()
call_big_py()
call_big_go()
