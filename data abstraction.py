class abstrc():
    __class_varbl = "abstrc"
    def __init__(self):
        self.__absrt_instvar="instat"
        print("i am in abstrc init")
    def __abst_method(self):
        print("i am inside the __abst_method and calling the absrt_instvar ",self.__absrt_instvar,abstrc.__class_varbl)
obj=abstrc()
#obj.__abst_method
print(obj._abstrc__absrt_instvar)
print(dir(abstrc))
obj._abstrc__abst_method()
print(abstrc._abstrc__class_varbl)
abstrc._abstrc__class_varbl = "static"
print(abstrc._abstrc__class_varbl)
obj._abstrc__abst_method()