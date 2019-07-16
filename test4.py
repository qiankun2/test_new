from multiprocessing import Process
import time
import os

class MyProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        print("进程为:%s 父进程为:%s" %(os.getpid(),os.getppid()))
        print("my name is",self.name)

if __name__ == "__main__":
    p_one = MyProcess("张三")
    p_two = MyProcess("李四")
    p_thr = MyProcess("王五")

    p_one.start()
    p_two.start()
    p_thr.run()

    p_one.join()
    p_two.join()
    #p_thr.join()

    print("主进程结束")