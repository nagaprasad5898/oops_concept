class family():
    relation="couples" #static or class variables
    def __init__(self,male,female):
        print("hi")
        self.male=male       #instatanious variables
        self.female=female
    def parentes(self,name):
        self.name = name
        print("{} and {} both are {} parents".format(self.male,self.female,self.name))
        #instatanious method
    @classmethod
    def grandparents(cls):
        print("{}".format(cls.relation))
    @staticmethod
    def siblings(a,b):
            print(a+"and "+b+"both are siblings")
obj1=family("kanna","lucky")#init or initialization method
obj1.parentes("chaithu") #acessing the instatanious method
family.grandparents()#accessing the class methods
family.relation="lovely couple" # changeing the static variable value
family.grandparents() #calling the cbhanged static  variable
family.siblings("kanna","sai")#statci method calling
obj=family#it wont print the contatent of init  because we are not placing the () it is also called init method calling
print(obj)
print(id(obj))
print(id(obj1))

obj.parentes(obj1,"kanna")