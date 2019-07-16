from multiprocessing import Pool
import time

def func(num):
    num += 1
    return num

if __name__ == "__main__":
    p = Pool(5)
    start = time.time()
    l = []
    for i in range(100):
        res = p.apply_async(func,args=(i,))
        l.append(res)
    p.close()
    p.join()
    [print(i.get()) for i in l]
    print(time.time()-start)