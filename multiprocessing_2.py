# -*- coding: utf-8 -*-

import multiprocessing as mp
import time

def job(x):
    result = 0
    for i in range(1000000):
        result = result + x**2 + x**3 
    
    return result

def multicore(data):
    pool = mp.Pool()
    res = pool.map(job, data)
    print(res)
    
#data = range(10)
data = range(9, -1, -1)
if __name__ == '__main__':
    print('your cpu count: %g'%(mp.cpu_count()))
    
    time_start = time.time()
    multicore(data)
    time_ellapsed = time.time() - time_start
    print('multicore time: %g, average: %g'%(time_ellapsed, time_ellapsed / len(data)))
    print('multicore time multiply cpu core: %g'%(time_ellapsed / len(data) * mp.cpu_count()))
    
    for i in data:
        time_start = time.time()
        job(i)
        print('job %g time: %g'%(i, time.time() - time_start))
    
    pool = mp.Pool()
    time_start = time.time()
    multi_res = [pool.apply_async(job, (i,)) for i in data]
    print([res.get() for res in multi_res])
    time_ellapsed = time.time() - time_start
    print('apply_async time: %g, average: %g'%(time_ellapsed, time_ellapsed / len(data)))
    