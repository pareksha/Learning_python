class Workers:
    salary_per_hr = 200
    bonus = 500
    def __init__(self,name,working_hours):
        self.name = name
        self.working_hours = working_hours

    def printing(self):
        return "{} works {} hours.".format(self.name,self.working_hours)


    def salary(self):
        self.salary =  self.salary_per_hr * self.working_hours

    def printing_again(self):
        return "{} with {} working hours has {} salary.".format(self.name,self.working_hours,self.salary)

    @classmethod
    def additional_salary(cls,additional):
        cls.bonus = additional

    @classmethod
    def from_string(cls,st):
        name, hours = st.split("/")
        working_hours = int(hours)
        return cls(name,working_hours)

    def final_salary(self):
        return "Final salary is : {}".format(self.salary + int(Workers.bonus))

    @staticmethod
    def end():
        return "THE END"

Abhi = Workers("Abhi",8)
Ajay = Workers("Ajay",9)

print(Workers.printing(Abhi))
print(Workers.printing(Ajay))

print("Print again: ")

Workers.salary(Abhi)
Workers.salary(Ajay)

print(Workers.printing_again(Abhi))
print(Workers.printing_again(Ajay))


st_1 = "Raju/5"
new_st_1 = Workers.from_string(st_1)
Workers.salary(new_st_1)



bn = input("Enter the Diwali bonus you want to give to the employee: ")

Workers.additional_salary(bn)
print("Bonus is: ")
print(Workers.bonus)


print(Workers.final_salary(Abhi))
print(Workers.final_salary(Ajay))
print(Workers.final_salary(new_st_1))

print(Workers.end())
