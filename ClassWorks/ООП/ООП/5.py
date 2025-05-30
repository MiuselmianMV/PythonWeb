# Object
# Начиная с 3-й версии в языке программирования Python все классы неявно имеют один общий суперкласс - object и все классы по умолчанию наследуют его методы.

# Одним из наиболее используемых методов класса object является метод __str__(). Когда необходимо получить строковое представление объекта или вывести объект в виде строки, то Python как раз вызывает этот метод. И при определении класса хорошей практикой считается переопределение этого метода.

class Person:
    def __init__(self, name, age):
        self.name = name  # устанавливаем имя
        self.age = age  # устанавливаем возраст
 
    def display_info(self):
        print(self)
        # print(self.__str__())     # или так
 
    def __str__(self):
        return f"Name: {self.name}  Age: {self.age}"
 
 
tom = Person("Tom", 23)
print(tom)      # Name: Tom  Age: 23
tom.display_info()  # Name: Tom  Age: 23