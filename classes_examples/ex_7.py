class Operations:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def sub(x,y):
        return self.x - self.y

class Complex_Operations:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.operation = Operations(x,y) #create an instance of the class in another class
                                         #also define and declare variables in the previous class
    def multiply(self):
        return self.x*self.y
    def add(self):
        return self.operation.add()

obj_1 = Complex_Operations(3,4)
print(obj_1.add())
