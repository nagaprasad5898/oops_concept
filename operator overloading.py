class cal:
    def __init__(self,num):
        self.num=num

obj=cal(1)
obi1=cal(2)
#print(obj+obj1)#==>it wont add 2class at a time
#to add 2class we need to def magical methods lets see how to defind magical methods
class cal1():
    def __init__(self,num):
        self.num=num
    def __str__(self):
        return self.num
    def __add__(self, other):
        num1=self.num+other.num
        return num1
    #defng __radd__ to add one class objct with prsnt class
    def __radd__(self, other):
        num1=self.num+other.num
        return num1
obj2=cal1(10)
obj3=cal1(58)
print(obj2+obj3)
obj2+=obj3
print("obj2:",obj2)
#we cann"t add one another class obj to prsnt class obj
# to add those we want to defind another function call __radd__
a=obj+obj2
print(a)
