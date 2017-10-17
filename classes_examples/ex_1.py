class Siblings:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def name_age(self):
        print("{} is of {} years.".format(self.name,self.age))

pecha = Siblings("pecha",18)
bhaiya = Siblings("Gourav",22)

Siblings.name_age(pecha)
bhaiya.name_age()
