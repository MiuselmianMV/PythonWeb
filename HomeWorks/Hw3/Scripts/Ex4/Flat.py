class Flat:
    def __init__(self, area: float, price: float):
        self.__area = area
        self.__price = price

    def __eq__(self, other):
        return self.__area == other.__area

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return self.__price > other.__price

    def __lt__(self, other):
        return self.__price < other.__price

    def __ge__(self, other):
        return self.__price >= other.__price

    def __le__(self, other):
        return self.__price <= other.__price

    def __str__(self):
        return f"Flat(area={self.__area}, price={self.__price})"

def demonstration():
    
    f1 = Flat(40.5, 50000)
    f2 = Flat(50, 60000)
    f3 = Flat(40.5, 53000)

    print("Проверка на равенство площадей:")
    print("f1 == f2:", f1 == f2)
    print("f1 == f3:", f1 == f3)
    print("f1 != f2:", f1 != f2)
    
    print("\nСравнение по цене:")
    print("f1 > f2:", f1 > f2)
    print("f2 < f3:", f2 < f3)
    print("f2 >= f1:", f2 >= f1)
    print("f3 <= f1:", f3 <= f1)

    print("\nИнформация о квартирах:")
    print("f1:", f1)
    print("f2:", f2)
    print("f3:", f3)




    
