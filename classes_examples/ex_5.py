class Students:
    def __init__(self,first,last):
        self.first = first
        self.last = last

    def fullname(self):
        return "{} {}".format(self.first,self.last)

    def __repr__(self):
        return "{}".format(self.fullname())

    def __str__(self):
        return "Fullname is {}".format(self.fullname())

    def __add__(self):
        return self.first + self.last

    #def __len__(self):
    #    return len(self.first)

st_1 = Students("Pareksha","Manchanda")
print(st_1)
print(repr(st_1))
print(st_1.__repr__())
#print(len(st_1))
print(len(st_1.first))
