class IntegerSet:
    def __init__(self, numbers: list[int]):
        self.numbers = numbers

    def get_sum(self):
        return sum(self.numbers)

    def get_average(self):
        if not self.numbers:
            return 0
        return sum(self.numbers) / len(self.numbers)

    def get_max(self):
        return max(self.numbers)

    def get_min(self):
        return min(self.numbers)
