class students() :
    def __init__(self,name,age,m1,m2) :
        self.name = name
        self.age = age
        self.sub = self.subject(m1,m2)
        self.sub.marks()#inner class variable
    def details(self) :
        print("name : {} \n age : {}".format(self.name,self.age))
        self.sub.marks()
    def info(self) :
        print(self.name,self.age)
    class subject() :
        def __init__(self,m1,m2):
            self.m1 = m1
            self.m2 = m2
        def marks(self):
            print(self.m1,self.m2)
obj=students("harish",22,10,20)
#print(obj.name)
#print(obj.age)
#obj.details()
#obj.info()
#obj.sub.marks()
#print(obj.sub.m1)#calling the inner class varabiles from out side a class
#'''
obj2 = students.subject(20,30)
obj2.marks()
print(obj2.m2)
'''
obj.details()
obj.sub.marks()
print(obj.sub.m1)
'''