#1. В классе Person определен конструктор - функция __init__. Конструктор должен принимать как минимум один параметр ссылку на текущий объект - self.

# class Person:
#     # конструктор
#     def __init__(self):
#         print("Создание объекта Person")
 
# tom = Person()      # Создание объекта Person




# 2.Атрибуты хранят состояние объекта. Для определения и установки атрибутов внутри класса можно применять слово self. 
# class Person:
 
#     def __init__(self, name, age):
#         self.name = name    # имя человека
#         self.age = age        # возраст человека
 
 
# tom = Person("Tom", 22)
 
# # обращение к атрибутам
# # получение значений
# print(tom.name)     # Tom
# print(tom.age)      # 22
# # изменение значения
# tom.age = 37
# print(tom.age)      # 37

#3. ---------  Методы класса
# class Person:
 
#     def __init__(self, name, age):
#         self.name = name        # имя человека
#         self.age = age          # возраст человека
     
#     def display_info(self):
#         print(f"Name: {self.name}  Age: {self.age}")
 
 
# tom = Person("Tom", 22)
# tom.display_info()      # Name: Tom  Age: 22
 
# bob = Person("Bob", 43)
# bob.display_info()      # Name: Bob  Age: 43

#4.----Деструкторы 
# class Person:
  
#     def __init__(self, name):
#         self.name = name
#         print("Создан человек с именем", self.name)
     
#     def __del__(self):
#         print("Удален человек с именем", self.name)
  
# tom = Person("Tom")