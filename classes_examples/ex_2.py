from textwrap import dedent
class Students:
    num_of_students = 0
    num_of_friends = 2

    def __init__(self,name,roll_no,email):
        self.name = name
        self.roll_no = roll_no
        self.email = email
        Students.num_of_students += 1

    def printing(self):
        return dedent("""
    Name = {}
    Roll Number = {}
    email = {}
    """.format(self.name,self.roll_no,self.email))

    def friends(self):
        return "{}".format(self.num_of_friends)


print(Students.num_of_students)

Nandita = Students("Nandita",35,"nanditasharma@gmail.com")
Pareksha = Students("Pareksha",18,"pareksha.manchanda@gmail.com")
Purnima = Students("Purnima",22,"purnaima@yahoo.com")

print(Students.num_of_students)

print(Nandita.printing())
print(Students.printing(Pareksha))
print(Purnima.printing())



print(Students.num_of_friends)
Nandita.num_of_friends = 3
print(Nandita.__dict__)
print(Nandita.num_of_friends)
