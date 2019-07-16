from multiprocessing import Process
import time

def func_one(name):
    print("my name is",name)
    time.sleep(1)

def func_two(age):
    print("my age is",age)
    time.sleep(5)

if __name__ == "__main__":
    lst_one = []
    lst_two = []
    for i in range(5):
        p_one = Process(target=func_one,args=("小华",))
        p_two = Process(target=func_two,args=("27",))
        p_one.start()
        p_two.start()
        lst_two.append(p_two)
        [p_two.join() for p_two in lst_two]
    print("end")