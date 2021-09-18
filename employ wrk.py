class employe():
#    print("i am inside the employee class")
    def __init__(self,name):
        self.name= name
        print("i am inside the init function {}".format(self.name))
    def working(self,work):
        print("i am working in {}".format(work))
    def singing(self):
        print("{} can sing".format(self.name))
    def dancing(self):
        print(self.name +" can dance")
    def compar(self,other):
        self.other=other
        if obj.name == other.name:
            print("yes")
        else:
            print("no")

obj=employe("kanna")
obj1=employe("kanna")
obj2=employe("kanna")
obj1.name="lucky"
obj2.name="tkc"
obj.working("freelancer")
obj.singing()
obj.dancing()
obj1.working("filme industry")
obj1.dancing()
obj1.singing()
obj2.working("railway")
obj2.dancing()
obj.singing()
obj.compar(obj1)