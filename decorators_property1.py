class student():
    def __init__(self,name):
        self.__name=name
    def per(self):
        print("my name is :",self.__name)

    def getter(self):
         print(self.__name)
    def setter(self,ch_name):
        self.__name = ch_name
    def delt(self):
        del self.__name
    name = property(getter,setter,delt)
s=student("kanna")
s.per()
s.name="luck"
s.per()
del s.name
s.name="kannalucky"
s.per()

