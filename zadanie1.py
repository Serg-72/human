
from os import name


class Car:
    def __init__(self, name = None, color = None, speed = None, trailer = None):
        self.__name = name
        self.color = color  
        self.speed = speed
        self.trailer = trailer
    def garage(self):
        print(f" Название: {self.__name}, Цвет: {self.color}, Скорость: { self.speed}, Прицеп: {self.trailer}")
    
car1 = Car("Калина", "Зеленый", " max = 100 км/ч")
car1.garage()

class Tractor(Car):
    def __init__(self, trailer = None):
        self.trailer = trailer
    def garage(self):
        print(self.__name, self.color, self.speed, self.trailer)
tr1 = Car("МТЗ", "Синий", "max = 60 км/ч", " max 6 тон")
tr1.garage()   
color1 = Car("Калина", "Зеленый", " max = 100 км/ч")
color1.color = "Красный"
color1.garage() 

     @property
     def name(self):
         return self.__name
     
     @name.setter
     
     def set_name(self, name):
        self.__name = name
        
   # def get__name(self, name):
       # self.__name = name
   # def garage(self):
       # print(f" Название: {self.__name}, Цвет: {self.color}, Скорость: { self.speed}, Прицеп: {self.trailer}")

#tr1 = Car("МТЗ", "Синий", "max = 60 км/ч", " max 6 тон")
tr1.set_name = "Беларус"
tr1.garage()
