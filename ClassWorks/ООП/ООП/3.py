# --  Наследование позволяет создавать новый класс на основе уже существующего класса. Наряду с инкапсуляцией наследование является одним из краеугольных камней объектно-ориентированного программирования.

# Ключевыми понятиями наследования являются подкласс и суперкласс. Подкласс наследует от суперкласса все публичные атрибуты и методы. Суперкласс еще называется базовым (base class) или родительским (parent class), а подкласс - производным (derived class) или дочерним (child class).

# class подкласс (суперкласс):
#     методы_подкласса

# class Person:
 
#     def __init__(self, name):
#         self.__name = name   # имя человека
 
#     @property
#     def name(self):
#         return self.__name
 
#     def display_info(self):
#         print(f"Name: {self.__name} ")
 
 
# class Employee(Person):
 
#     def work(self):
#         print(f"{self.name} works")
 
 
# tom = Employee("Tom")
# print(tom.name)     # Tom
# tom.display_info()  # Name: Tom 
# tom.work()          # Tom works



# Множественное наследование
#  класс работника
# class Employee:
#     def work(self):
#         print("Employee works")
 
 
# #  класс студента
# class Student:
#     def study(self):
#         print("Student studies")
 
 
# class WorkingStudent(Employee, Student):        # Наследование от классов Employee и Student
#     pass 
 
# # класс работающего студента
# tom = WorkingStudent()
# tom.work()      # Employee works
# tom.study()     # Student studies


# -- проверка на тип !!! 

# class Person:
 
#     def __init__(self, name):
#         self.__name = name   # имя человека
 
#     @property
#     def name(self):
#         return self.__name
 
#     def do_nothing(self):
#         print(f"{self.name} does nothing")
 
 
# #  класс работника
# class Employee(Person):
 
#     def work(self):
#         print(f"{self.name} works")
 
 
# #  класс студента
# class Student(Person):
 
#     def study(self):
#         print(f"{self.name} studies")
 
 
# def act(person):
#     if isinstance(person, Student):
#         person.study()
#     elif isinstance(person, Employee):
#         person.work()
#     elif isinstance(person, Person):
#         person.do_nothing()
 
 
# tom = Employee("Tom")
# bob = Student("Bob")
# sam = Person("Sam")
 
# act(tom)    # Tom works
# act(bob)    # Bob studies
# act(sam)    # Sam does nothing
