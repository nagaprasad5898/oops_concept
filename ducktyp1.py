#duck method is using the same method in differnt place
# to get different values from same procedure lets take an example
#schl have students method as show in below and we have another
# class called clg with same method we have created an another class called education and
# hear we creant an method to call those method by passing class name in that method as show in below
class schl():
    def students(self):
        print("all are under 16yrs old")
class clg():
    def students(self):
        print("all are above 16yrs old")
class education():
    def dep(self,departmnt):
        departmnt.students()
departmnt1=schl()#the abjct we are passing must have the method 
departmnt2 =clg()
obj=education()
obj.dep(departmnt1)
obj.dep(departmnt2)