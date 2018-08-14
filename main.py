import time
from threading import Thread

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
    obj.arr_sorting(40)
    return

@timeit
def call_small_go():
    lib = cdll.LoadLibrary('./golang_bubl_sort.so')
    lib.arr_sorting.argtypes = [c_longlong]
    lib.arr_sorting.restype = None
    lib.arr_sorting(40)

@timeit
def call_big_py():
    obj.arr_sorting(40000)
    return

@timeit
def call_big_go():
    lib = cdll.LoadLibrary('./golang_bubl_sort.so')
    lib.arr_sorting.argtypes = [c_longlong]
    lib.arr_sorting.restype = None
    lib.arr_sorting(40000)

call_small_go()
call_small_py()
call_big_go()
call_big_py()
#ts_py = Thread(target = call_small_py, args = [])
#ts_go = Thread(target = call_small_go, args = [])
#tb_py = Thread(target = call_big_py, args = [])
#tb_go = Thread(target = call_big_go, args = [])
#ts_py.start()
#ts_go.start()
#tb_py.start()
#tb_go.start()