class Warriors(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        return f"Name : {self.name}\nAge : {self.age}"

class Province(object):
    def __init__(self,names,name,age):
        self.name = name
        self.age = age
        self.warrior_name = Warriors(self.name,self.age)
        self.names = names

    def province_under(self):
        print("Province {} is under warrior:".format(self.names))
        print(self.warrior_name.info())


war_1 = Warriors("Ajay",25)
war_2 = Warriors("Abhay",30)

prov_1 = Province("Mumbai","Ajay",25)
prov_2 = Province("Delhi","Abhay",30)


prov_1.province_under()
prov_2.province_under()
