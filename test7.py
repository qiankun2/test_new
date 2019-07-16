from multiprocessing import Pool
import time

#def func(num):
    #num += 1
    #return num

#if __name__ == "__main__":
    #p = Pool(5)
    #start = time.time()
    #for i in range(100):
        #res = p.apply(func,args=(i,))
        #print(res)
    #print(time.time() - start)




def func2(a,*args):
  print("我是形参a:",a)
  print("我是形参args:",args)

func2(1,2,3,4,5)
print("-------------------------------------------------------------------------------")

def func3(a,*args,**dict):
    print("我是形参a:",a)
    print("我是形参*args;",args)
    print("我是形参**other;",dict)

def func4(a,b,c=0,*args,name,age,**kw):
    print('a:',a)
    print('b:',b)
    print('c:',c)
    print('args:',args)
    print("name:",name)
    print('age:', age)
    print('kw:',kw)

func3(1,2,3,4,5,name="小明",age=25)

args = (1,2,3,4,5)
kw = {'z':1}
func4(1,2,3,*args,name='大兵',age=35,**kw)
