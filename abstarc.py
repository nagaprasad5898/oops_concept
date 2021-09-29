#it dosnt any defanation its only have declaration
from  abc import ABC,abstractmethod
class childrns(ABC):
    @abstractmethod
    def names(self):
        pass
    def age(self,b):
        print("my age is ",b)
class students(childrns):
    def names(self,a):
        print("my name is ",a)
obj = students()
obj.names("kanna")
obj.age(25)