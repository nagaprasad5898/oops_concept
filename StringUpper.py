class string:
    def getstring(self):
        self.n=input("enter a string")
        return self.n
    def printstring(self):
        n1=self.n.upper()
        return n1
obj=string()
print(obj.getstring())
print(obj.printstring())
