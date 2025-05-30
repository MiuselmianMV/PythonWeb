# Задание 2
# Создайте класс Complex (комплексное число). Более 
# подробно ознакомиться с комплексными числами можно 
# по ссылке.
# Создайте перегруженные операторы для реализации 
# арифметических операций для по работе с комплексными 
# числами (операции +, -, *, /)

class Complex:

    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)


    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        denominator = other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real, imag)

    def __str__(self):
        sign = "+" if self.imag >= 0 else "-"
        return f"{self.real} {sign} {abs(self.imag)}i"


def demonstration():
    a = Complex(2, 3)
    b = Complex(1, -4)
    print(f"a + b = {a+b}")     # 3 - 1i
    print(f"a - b = {a-b}")     # 1 + 7i
    print(f"a * b = {a*b}")     # 14 - 5i
    print(f"a / b = {a/b}")     # -0.6470588235294118 + 0.47058823529411764i
