class father():
    def __init__(self,dad_name,dad_age):
        self.name=dad_name
        self.age=dad_age
    def daddetalis(self):
        print("i am {} and my age {}".format(self.name,self.age))
class mother():
    def __init__(self,mom_name,mom_age):
        self.name1=mom_name
        self.age1=mom_age
    def momdetails(self):
        print("i am {} and my age {}".format(self.name1,self.age1))
class child(father,mother):
    def __init__(self,dad_name,dad_age,mom_name,mom_age,son_name):
        self.name2=son_name
        father.__init__(self,dad_name,dad_age)
        mother.__init__(self,mom_name,mom_age)
 #       mother.__init__(self,mom_name,mom_age)
    def family(self):
        print("i am {} and my father {} and his age {} my mother {} and her age {}".format(self.name2,self.name,self.age,self.name1,self.age1))
obj=child("venkateswara rao",55,"annapurna",45,"kanna")
obj.family()
obj1=mother("annapurna",45)
obj1.momdetails()