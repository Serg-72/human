
""" lass Car:
    
    def __init__(self, Model, Name, Color, Prise):
        self.Model = Model
        self.Name = Name
        self.Color = Color
        self.Prise = Prise
    def garage(self):
        print(self.Model, self.Name, self.Color, self.Prise)
        
car1 = Car( "Лада", "Калина", "Красный","1200 $")
car2 = Car("Лада", "Приора", " Зеленый", "1000 $") 
car3 = Car("Лада", "Веста", "Белый", "1800 $") 
      
car3.garage() """


#n = 27
#for i in range(n):
    #print("^" , end = " ")
#rus = [["А,а", "Б,б", "В,в"],"/n"["Г,г", "Д,д","Е,е"]]
#for i in range(n):       
       #print("^" , end = " "),
       #["Г,г", "Д,д","Е,е"]
       
#print(rus)




import time

class Person:
    def __init__(self, name=None, age=None, sex=None, city=None, country=None):
        self.name = name
        self.age = age
        self.sex = sex
        self.city = city
        self.country = country

    def walk(self):
        print("Walk")

class Worker(Person):
    def __init__(self, salary, name=None, age=None, sex=None, city=None, country=None):
        super().__init__(name=name, age=age, sex=sex, city=city, country=country)
        self.fatigue = 0
        self.salary = salary
    
    def work(self):
        self.fatigue += 10
        if self.fatigue >= 100:
            self.relax()
    
    def relax(self):
        while self.fatigue > 30:
            print('Relax')
            self.fatigue -= 5
    

class Teacher(Worker):
    def __init__(salary, name=None, age=None, sex=None, city=None, country=None):
        super().__init__(salary, name=name, age=age, sex=sex, city=city, country=country)

    def work(self):
        print("Учу детей")
        super().work()
    
class Driver(Worker):
    def __init__(salary, name=None, age=None, sex=None, city=None, country=None):
        super().__init__(salary, name=name, age=age, sex=sex, city=city, country=country)

    def work(self):
        print("Кручу баранку")
        super().work()

t = Teacher()
d = Driver()

while True:
    t.work()
    d.work()
    time.sleep(1)












    
    
