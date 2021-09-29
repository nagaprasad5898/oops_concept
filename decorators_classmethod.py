class student():
    clg = "mic"
    def __init__(self,name):
        self.name=name
    def details(self):
        print("i am {} and from {}".format(self.name,student.clg))
    @classmethod
    def clas(cls,roll):
        print("i am from {} collage and my roll is {}".format(student.clg,roll))
print(student.clg)
student.clas(258)