class string:
    def getstring(self):
        self.n=input("enter a string")
        return self.n
    def printstring(self):
        self.n1=self.n.upper()
        return self.n1
obj=string()
print(obj.getstring())
print(obj.printstring())