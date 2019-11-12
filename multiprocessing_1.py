# -*- coding: utf-8 -*-

import multiprocessing as mp
import time

def job(a,d, q):
    result = 0;
    
    for i in range(10000000):
        result = result + a**10 + d**10;
    q.put(result)
    print(result)
    
if __name__ == '__main__':
    print('your cpu count: %g'%(mp.cpu_count()))
    a, b = 1, 2
    time_start = time.time()
    q = mp.Queue()
    mp_list = []
    for i in range(10):
        p1 = mp.Process(target=job,args=(a, b, q))
        mp_list.append(p1)
    [_.start() for _ in mp_list]
    [_.join for _ in mp_list]
    
    for i in range(len(mp_list)):
        print(q.get())
    print('done')
    print('time elapsed: %g'%(time.time() - time_start))
    print('time average: %g'%((time.time() - time_start) / len(mp_list)))
    time_start = time.time()
    job(a, b, q)
    print('time no multi: %g'%(time.time() - time_start))
    