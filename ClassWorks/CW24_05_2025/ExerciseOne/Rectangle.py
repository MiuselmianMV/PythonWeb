class Rectangle:
    def __init__(self, a: int, b: int):
        self.__width = a
        self.__length = b

    def area(self):
        return self.__width * self.__length

    def perimeter(self):
        return 2 * self.__width + 2 * self.__length

    @property
    def width(self):
        return self.__width

    @property
    def length(self):
        return self.__length

    @width.setter
    def width(self, width: int):
        self.__width = width

    @length.setter
    def length(self, length:int):
        self.__length = length


