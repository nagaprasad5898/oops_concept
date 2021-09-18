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
obj=frinds("kanna","8801124040")
obj.details()
obj1=roommets("bapatla","kanna",8801124040)
obj1.details()

