#with paramtrs
def fun1(arg):
    def fun2(fun):
        def fun3(*a,**b):
            print(arg)
            z=fun(*a,**b)
        return fun3
    return fun2
class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    @fun1(10)
    def cal1(self):
        c=self.a
        d=self.b
        print(c**d)
obj=cal(5,8)
obj.cal1()
