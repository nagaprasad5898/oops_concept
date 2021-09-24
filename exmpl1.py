class it():
    def __init__(self):
        self.a=1
    def __iter__(self):
        return self
    def __next__(self):
        y=self.a
        if self.a<10:
            self.a=self.a+1
            return y
        else:
            raise StopIteration
obj=it()
print(obj.__next__())
for i in obj:
    print(i)
