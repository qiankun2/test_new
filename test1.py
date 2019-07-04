import os
from multiprocessing import Process

def func_one():
    print("This is son_one")
    print("son_one:%s father:%s" %(os.getpid(),os.getppid()))

def func_two():
    print("This is son_two")
    print("son_two:%s father:%s" %(os.getpid(),os.getppid()))

if __name__ == "__main__":
      p_one = Process(target=func_one)
      p_two = Process(target=func_two)
      p_one.start()
      p_two.start()
      print("son:%s father:%s" %(os.getpid(),os.getppid()))
