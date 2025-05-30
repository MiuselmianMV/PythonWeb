# Задание 3
# Вам необходимо создать класс Airplane (самолет). 
# С помощью перегрузки операторов реализовать: 
# ■ Проверка на равенство типов самолетов (операция 
# = =); 
# ■ Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
# ■ Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции > 
# < <= >=)

class Airplane:
    def __init__(self, plane_type: str, max_passengers: int, current_passengers: int = 0):
        self.__plane_type = plane_type
        self.__max_passengers = max_passengers
        self.__current_passengers = current_passengers

    def __eq__(self, other):
        return self.__plane_type == other.__plane_type
    
    def __ne__(self, other):
        return not (self == other)

    def __add__(self, value):
        new_passengers = min(self.__current_passengers + value, self.__max_passengers)
        return Airplane(self.__plane_type, self.__max_passengers, new_passengers)

    def __sub__(self, value):
        new_passengers = max(self.__current_passengers - value, 0)
        return Airplane(self.__plane_type, self.__max_passengers, new_passengers)

    def __iadd__(self, value):
        self.__current_passengers = min(self.__current_passengers + value, self.__max_passengers)
        return self

    def __isub__(self, value):
        self.__current_passengers = max(self.__current_passengers - value, 0)
        return self

    def __gt__(self, other):
        return self.__max_passengers > other.__max_passengers

    def __lt__(self, other):
        return self.__max_passengers < other.__max_passengers

    def __ge__(self, other):
        return self.__max_passengers >= other.__max_passengers

    def __le__(self, other):
        return self.__max_passengers <= other.__max_passengers

    def __str__(self):
        return f"Airplane(type={self.__plane_type}, max={self.__max_passengers}, current={self.__current_passengers})"


def demonstration():
    a1 = Airplane("Boeing 737", 180, 50)
    a2 = Airplane("Airbus A320", 160, 120)
    a3 = Airplane("Boeing 737", 150, 20)

    print(f"a1: {a1}")
    print(f"a2: {a2}")
    print(f"a3: {a3}")

    print("Проверка на равенство типов:")
    print("a1 == a2:", a1 == a2)
    print("a1 == a3:", a1 == a3)

    print("\nСравнение по максимально возможному количеству пассажиров:")
    print("a1 > a2:", a1 > a2)
    print("a1 < a3:", a1 < a3)



    print("\na4 = a1 + 100:")
    a4 = a1 + 100
    print("a4:", a4)

    print("\na5 = a1 - 30:")
    a5 = a1 - 30
    print("a5:", a5)

    print("\na1 += 200:")
    a1 += 200
    print("a1:", a1)

    print("\na1 -= 300:")
    a1 -= 300
    print("a1:", a1)




