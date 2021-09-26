#by using the property method and setting and deleting
class student():
    def __init__(self,name):
        self.name = name
    @property
    def details(self):
        return self.name
    @details.setter
    def details(self,name3):
        self.name= name3
    @details.deleter
    def details(self):
        del self.name


obj=student("kanna")
print(obj.details)
obj.name="lucky"
print(obj.details)
del obj.details

obj.name ="kannalucky"
print(obj.details)

