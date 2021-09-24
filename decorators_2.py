#using the decorator function inside a class
#1st defind a class
def func1(fun):
    def func2(*a,**b):
        print("in funct2 befor fun excution")
        fun(*a,**b)
        print("in funct2 after fun excution")
    return func2
#now creat a class
class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    @func1
    def cal1(self):
        print(self.a*self.b)
obj=cal(5,8)
obj.cal1()
