class circle:
    PI=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        a=3.14*self.radius*self.radius
        return a
obj=circle(5)
print(obj.area())
