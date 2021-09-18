#definig an empty class and calling
class kanna:
#    print("hi kanna")
    pass
#obj=kanna()#it will give class name with address location ==> (__main__.kanna object at 0x0000026E1B378040)
#print(obj)
#print(kanna)#it just print type and name of the class ==>
#defining class with init method(constructor)
class lucky():
#    print("this is lucky class")
    def __init__(self,name):
        self.name=name
        print("i am inside init method ",__name__)
obj1=lucky("kanna")
#print(lucky("kanna"))
#defining class with method
class kannalucky():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def py(self,name,age,gender):
        print("i am "+name+" and my age is "+ age +" and my gender is "+ gender)
obj2=kannalucky("kanna","24")
obj2.py("kanna","24","male")

