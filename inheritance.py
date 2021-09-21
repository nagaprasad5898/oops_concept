class frinds():
    def __init__(self,names,numbers):
        self.names=names
        self.numbers=numbers
    def details(self):
        print("his name is {} and his number is {}".format(self.names,self.numbers))
class roommets(frinds):
    def __init__(self,place,names,numbers):
        self.place=place
        frinds.__init__(self,names,numbers)
        #self.batch=batch
    def details(self):
        print("his name {} and he is from {} and mobile number {}".format(self.names,self.place,self.numbers))
class work(roommets):
    def __init__(self,job,name,place,number):
        roommets.__init__(self,place,name,number)
        self.job=job
    def details(self):
        print("{} is from {} and he use to do {} and his number is {}".format(self.names,self.place,self.job,self.numbers))

obj=frinds("kanna","8801124040")
obj.details()
obj1=roommets("bapatla","kanna",8801124040)
obj1.details()
obj2=work("it","kanna","vijayawada",8801124040)

