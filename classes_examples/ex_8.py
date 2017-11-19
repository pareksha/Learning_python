class Salary:
    def __init__(self,pay):
        self.pay = pay
    def total(self):
        return self.pay * 12
class Worker:
    def __init__(self,pay,extra):
        self.extra = extra
        self.pay = pay
    def total_salary(self):
        return "{}".format(self.pay.total() + self.extra)

obj_salary = Salary(20000)
obj_worker = Worker(obj_salary,2000)
print(obj_worker.total_salary())
