class Employee:
    raise_amount = 1.05

    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name,self.last_name)

    @property
    def email(self):
        return '{}.{}@mycompany.com'.format(self.first_name.lower(),self.last_name.lower())

    def apply_raise(self):
        return self.salary * self.raise_amount

