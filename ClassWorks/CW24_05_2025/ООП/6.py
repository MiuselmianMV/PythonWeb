#Перегрузка операции 
class Counter:
    def __init__(self, value):
        self.value = value
    # переопределение оператора сложения
    def __add__(self, other):
        return Counter(self.value + other.value)
     
counter1 = Counter(5)
counter2 = Counter(15)
counter3 = counter1 + counter2
print(counter3.value)       # 20


# Ряд операций призваны возвращать логическое значение True или False.
# class Counter:
#     def __init__(self, value):
#         self.value = value
         
#     def __gt__(self, other):
#         return self.value > other.value
#     def __lt__(self, other):
#         return self.value < other.value
 
     
# counter1 = Counter(1)
# counter2 = Counter(2)
     
# if counter1 > counter2: 
#     print("counter1 больше чем counter2")
# elif counter1 < counter2:
#     print("counter1 меньше чем counter2")
# else: 
#     print("counter1 и counter2 равны")

# Обращение по индексу 

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
         
#     def __getitem__(self, prop):
#         if prop == "name": return self.__name
#         elif prop == "age": return self.__age
#         return None
     
# tom = Person("Tom", 39)
 
# print("Name:", tom["name"])     # Name: Tom
# print("Age:", tom["age"])       # Age: 39
# print("Id:", tom["id"])         # Id: None


# Проверка наличия свойства
# Оператор in позволяет проверить наличие определенного значения в последовательности - некотором наборе значений:
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
         
#     def __contains__(self, prop):
#         if prop == "name" or prop == "age": return True
#         return False
     
# tom = Person("Tom", 39)
# print("name" in tom)        # True
# print("id" in tom)          # False


# Реализация операторов парами
# Некоторые операторы - операторы сравения удобнее реализовать парами. Если мы реализуем оператор ==, то можно сразу реализовать и оператор !=. Причем чтобы не прописывать одну и ту же логику по два раза, можно реализовать один оператор через другой:
# class Counter:
#     def __init__(self, value):
#         self.value = value
     
#     def __eq__(self, other): return self.value == other.value
#     def __ne__(self, other): return not (self == other)
     
#     def __gt__(self, other): return self.value > other.value
#     def __le__(self, other): return not (self > other)
     
#     def __lt__(self, other): return self.value < other.value
#     def __ge__(self, other): return not (self < other)
         
# c1 = Counter(1)
# c2 = Counter(2)
 
# print(c1 == c2)     # False
# print(c1 != c2)     # True
 
# print(c1 < c2)      # True
# print(c1 >= c2)     # False

