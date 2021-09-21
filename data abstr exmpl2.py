class students():
    def __init__(self,name,age):
        self.__school="bashyam"
        self.name=name
        self.age=age
        print("it is an students init")
        self.__info() #calling the internal instance method in init with
        # another name because to access this method when this
        #class was using
    def info(self):
        print("i am in student class")
    __info = info # assing the method name to another variable
class teachers(students):
    def __init__(self,name,age):
        students.__init__(self,name,age)
        print("it is an teachers init")
    def info(self):
        print("i am in teachers class")
obj=teachers("kanna",25)
obj.info()