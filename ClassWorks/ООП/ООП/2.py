# ---- Инкапсуляция 
# class Person:
#     def __init__(self, name, age):
#         self.__name = name    # устанавливаем имя
#         self.__age = age       # устанавливаем возраст
                  
#     def print_person(self):
#         print(f"Имя: {self.__name}\tВозраст: {self.__age}")
          
  
# tom = Person("Tom", 39)
# tom.__name = "Человек-паук"     # пытаемся изменить атрибут __name
# tom.__age = -129                # пытаемся изменить атрибут __
# tom.print_person()              # Имя: Tom        Возраст: 39



#2. При объявлении атрибута, имя которого начинается с двух прочерков, например, __attribute, Python в реальности определяет атрибута, который называется по шаблону _ClassName__atribute. То есть в случае выше будут создаваться атрибуты _Person__name и _Person__age. Поэтому к такому атрибуту мы сможем обратиться только из того же класса. Но не сможем обратиться вне этого класса.
# !!!! приватность атрибутов тут довольно относительна !!!

# class Person:
#     def __init__(self, name, age):
#         self.__name = name    # устанавливаем имя
#         self.__age = age       # устанавливаем возраст
                  
#     def print_person(self):
#         print(f"Имя: {self.__name}\tВозраст: {self.__age}")
          
  
# tom = Person("Tom", 39)
# tom._Person__name = "Человек-паук"     # изменяем атрибут __name
# tom.print_person()              # Имя: Человек-паук        Возраст: 39


#3------- set get
# class Person:
#     def __init__(self, name, age):
#         self.__name = name    # устанавливаем имя
#         self.__age = age       # устанавливаем возраст
 
#     # сеттер для установки возраста
#     def set_age(self, age):
#         if 0 < age < 110:
#             self.__age = age
#         else:
#             print("Недопустимый возраст")
 
#     # геттер для получения возраста
#     def get_age(self):
#         return self.__age
 
#     # геттер для получения имени
#     def get_name(self):
#         return self.__name
     
#     def print_person(self):
#         print(f"Имя: {self.__name}\tВозраст: {self.__age}")
          
  
# tom = Person("Tom", 39)
# tom.print_person()  # Имя: Tom  Возраст: 39
# tom.set_age(-3486)  # Недопустимый возраст
# tom.set_age(25)
# tom.print_person()  # Имя: Tom  Возраст: 25



# 4.Аннотации свойств
# Для создания свойства-геттера над свойством ставится аннотация @property.
# Для создания свойства-сеттера над свойством устанавливается аннотация имя_свойства_геттера.setter.
# class Person:
#     def __init__(self, name, age):
#         self.__name = name    # устанавливаем имя
#         self.__age = age       # устанавливаем возраст
 
#     # свойство-геттер
#     @property
#     def age(self):
#         return self.__age
#     # свойство-сеттер
#     @age.setter
#     def age(self, age):
#         if 0 < age < 110:
#             self.__age = age
#         else:
#             print("Недопустимый возраст")
 
#     @property
#     def name(self):
#         return self.__name
     
#     def print_person(self):
#         print(f"Имя: {self.__name}\tВозраст: {self.__age}")
          
  
# tom = Person("Tom", 39)
# tom.print_person()  # Имя: Tom  Возраст: 39
# tom.age = -3486     # Недопустимый возраст  (Обращение к сеттеру)
# print(tom.age)      # 39 (Обращение к геттеру)
# tom.age = 25        # (Обращение к сеттеру)
# tom.print_person()  # Имя: Tom  Возраст: 25

