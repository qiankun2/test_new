from multiprocessing import Process
import time

def func_one(name):
    print("my name is",name)
    time.sleep(2)
    print("this is func_one")

def func_two(name):
    print("my name is",name)
    time.sleep(2)
    print("this is func_two")

if __name__ == "__main__":
    p_one = Process(target=func_one,args=("小明",))
    p_two = Process(target=func_two,args=("大G",))
    p_one.run()
    #p_one.join()
    p_two.start()

