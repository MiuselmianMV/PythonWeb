class BankAccount:
    def __init__(self, number: int, amount: int):
        self.__account_number = number
        self.__balance = amount



    def withdraw(self, amount: int):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Остаток на балансе {self.__account_number} - {self.__balance}")
        else:
            print(f"Недостаточно средств на балансе {self.__account_number}. ")

    def add(self, amount: int):
        self.__balance += amount
        print(f"Отлично! теперь на балансе {self.__account_number} - {self.__balance}$")

    @property
    def balance(self):
        return self.__balance

    @property
    def account_number(self):
        return self.__account_number

    @balance.setter
    def balance(self, amount):
        self.__balance = amount

