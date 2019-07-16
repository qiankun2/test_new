from multiprocessing import Process

def func_one():
    global n
    n = 0
    print("在func_one中的n为%s" %n)

def func_two():
    global n
    n = 1
    print("在func_one中的n为%s" %n)

if __name__ == "__main__":
    n = 100
    p_one = Process(target=func_one())
    p_two = Process(target=func_two())
    p_one.start()
    p_two.run()
    print("主线程的n为%s" %n)