from ExerciseOne import *
from ExerciseTwo import *


def ex_1():
    frst = Rectangle(1,2)
    sec = Rectangle(3,5)

    print(f"First area - {frst.area()}")
    print(f"Second area - {sec.area()}")

    print(f"First perimeter - {frst.perimeter()}")
    print(f"Second perimeter - {sec.perimeter()}")

    bank1 = BankAccount(1, 1000)
    bank1.add(100)
    bank1.withdraw(100)
    bank1.withdraw(1000)

def ex_2():
    a = Library("asdf", "lenina", 123)
    print(a>1)
    print(a<1)
    print(a>=1)
    print(a<=1)
    print(a == 123)
    print(a != 123)


def main():
    # ex_1()
    ex_2()


if __name__ == "__main__":
    main()
