class lapy():
    "my lappy"
    compy = "lenova"
    def __init__(self,modal,ram,cpu):
        self.modal=modal
        self.ram=ram
        self.cpu=cpu
        print("i am in 1st init")

    def config(self):
        print(self.modal)
        print(self.cpu)
        print(self.ram)
        print(lapy.compy)
class studnt():
    def __init__(self,gracrd):
        self.gracrd= gracrd
        print("i am in 2nd  init")
    def config1(self):
        print("gracrd:",self.gracrd)
        print(lapy.compy)
class sch(studnt,lapy):
    def __init__(self,name,modal,ram,cpu,gracrd):
        self.name=name
        studnt.__init__(self,modal)
        lapy.__init__(self,modal,ram,cpu)
        print("i am in 3rd init")
kanna_lapy=sch("kanna","idea330","8gb","i5","2gb")
kanna_lapy.config()