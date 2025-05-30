class Library:
    def __init__(self, name: str, address: str, amount_of_books: int):
        self.__name = name
        self.__address = address
        self.__amount_of_books = amount_of_books

    def __add__(self, other):
        self.__amount_of_books += other

    def __iadd__(self, other):
        self.__amount_of_books += other

    def __sub__(self, other):
        self.__amount_of_books -= other

    def __isub__(self, other):
        self.__amount_of_books -= other

    def __gt__(self, other) -> bool:
        if self.__amount_of_books > other:
            return True
        return False

    def __lt__(self, other) -> bool:
        if self.__amount_of_books < other:
            return True
        return False

    def __ge__(self, other) -> bool:
        if self.__amount_of_books >= other:
            return True
        return False

    def __le__(self, other) -> bool:
        if self.__amount_of_books <= other:
            return True
        return False

    def __eq__(self, other):
        if self.__amount_of_books == other:
            return True
        return False

    def __ne__(self, other):
        return not (self == other)

