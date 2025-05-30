# Атрибуты класса (статические поля в компилируемых языках программирования)
# Кроме атрибутов объектов в классе можно определять атрибуты классов. Подобные атрибуты определяются в виде переменных уровня класса.
# class Person:
#     default_name = "Undefined"
 
#     def __init__(self, name):
#         if name:
#             self.name = name
#         else:
#             self.name = Person.default_name
 
 
# tom = Person("Tom")
# bob = Person("")
# print(tom.name)  # Tom
# print(bob.name)  # Undefined

# статические методы
# class Person:
#     __type = "Person"
 
#     @staticmethod
#     def print_type():
#         print(Person.__type)
 
 
# Person.print_type()     # Person - обращение к статическому методу через имя класса
 
# tom = Person()
# tom.print_type()     # Person - обращение к статическому методу через имя объекта