class rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        a=self.l*self.w
        return a
obj=rectangle(5,5)
print("area of rectangle is",obj.area())