from multiprocessing import Pool
import time

#建立线程要调用的方法
def func(num):
    num += 1
    return num

#建立接受主线程返回数据的回调函数胡
def call_back(p):
    p += 1
    print(p)

if __name__ == "__main__":
    #建立线程池对象，设置最大并发数为10
    p = Pool(10)

    #建立开始线程任务时间
    start = time.time()

    #建立100个线程任务
    l = []
    for i in range(100):
        #线程任务采用异步处理方式,把数据返回给回调函数
        res = p.apply_async(func,args=(i,),callback=call_back)
        l.append(res)
    p.close()
    p.join()

    #[print(l) for i in l]
    print(time.time()-start)
