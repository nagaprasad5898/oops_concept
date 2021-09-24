class shape:
        a=0
class square(shape):
    def  __init__(self,l):
        self.l=l
    def area(self):
        a=self.l*self.l
        return a
obj=square(5)
print(obj.area())
