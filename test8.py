from multiprocessing import Pool
import time

#进程要执行的函数
def func(i):
    i += 1
    return i #普通进程处理过的数据返回给主进程p1

#建立异步的回调函数
def call_back(p1):
    p1 += 1
    return p1

if __name__ == "__mina__":
    #建立一个进程对象
    p1 = Pool()
    for i in range(10):
        # p调用普通进程并接受其返回值，将返回值给回调函数处理
        p1.apply_async(func,args=(i,),callback=call_back)

        #异步处理任务，必须执行close()和 join()操作，并且不能颠倒顺序
        p1.close()
        p1.join()

