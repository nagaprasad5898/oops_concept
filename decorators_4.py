#with paramtrs
def fun1(arg):
    def fun2(fun):
        def fun3(*a):
            print(arg)

        return fun3
    return fun2
@fun1(51)
class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __call__(self):
        c=self.a
        d=self.b
        return (c**d)
obj=cal(5,8)
