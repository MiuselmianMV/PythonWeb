import math


# Задание 1
# Создайте класс Circle (окружность). Для данного 
# класса реализуйте ряд перегруженных операторов:
# ■ Проверка на равенство радиусов двух окружностей 
# (операция = =);
# ■ Сравнения длин двух окружностей (операции >, <, 
# <=,>=);
# ■ Пропорциональное изменение размеров окружности, 
# путем изменения ее радиуса (операции + - += -=).

class Circle:
    
    def __init__(self, rad:int):
        self.__radius = rad
        self.__circumference = math.pi * 2 * self.__radius

    
    def __str__(self):
        return f"Circle(radius={self.__radius}, circumference={self.__circumference:.2f})"


    def __add__(self, other):
        return Circle(self.__radius + other)
       

    def __iadd__(self, other):
        self.__radius += other
        self.__circumference = math.pi * 2 * self.__radius
        return self
        

    def __sub__(self, other):
        return Circle(self.__radius - other)

    def __isub__(self, other):        
        self.__radius -= other
        self.__circumference = math.pi * 2 * self.__radius
        return self


    def __gt__(self, other) -> bool:
        if self.__circumference > other.__circumference:
            return True
        return False

    def __lt__(self, other) -> bool:
        if self.__circumference < other.__circumference:
            return True
        return False

    def __ge__(self, other) -> bool:
        if self.__circumference >= other.__circumference:
            return True
        return False
    
    def __le__(self, other) -> bool:
        if self.__circumference <= other.__circumference:
            return True
        return False

    def __eq__(self, other):
        if self.__radius == other.__radius:
            return True
        return False

    def __ne__(self, other):
        return not (self == other)
    


def demonstration():
    c1 = Circle(5)
    c2 = Circle(7)
    c3 = Circle(5)
    print(f"1- {c1}\n2- {c2}\n3- {c3}")

    print("== Проверка на равенство радиусов ==")
    print()
    print("c1 == c2:", c1 == c2)
    print("c1 == c3:", c1 == c3)
    print("c1 != c2:", c1 != c2)

    print("\n== Сравнение длин окружностей ==")
    print()
    print("c1 > c2:", c1 > c2)
    print("c1 < c2:", c1 < c2)
    print("c1 >= c3:", c1 >= c3)
    print("c1 <= c2:", c1 <= c2)

    print("\n== Пропорциональное изменение радиуса (операции +, -) ==")
    print()
    
    print("Увеличим радиус c1 на 2 через +:")
    c4 = c1 + 2
    print(c4)
    print()
    print("Уменьшим радиус c2 на 1 через -:")
    c5 = c2 - 1
    print(c5)
    print()

    print("Инкрементируем радиус c1 через +=")
    c1 += 3
    print(c1)
    print()

    print("Декрементируем радиус c2 через -=")
    c2 -= 2
    print(c2)

demonstration()
