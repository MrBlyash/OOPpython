import random

class Encryptor:
    def __init__(self, *numbers):
        self._hidden_numbers = numbers
        self._operation = random.choice(["+", "-", "*", "/"])
    def _calculate(self):
        result = self._hidden_numbers[0]
        for num in self._hidden_numbers[1:]:
            if self._operation == "+":
                result += num
            elif self._operation == "-":
                result -= num
            elif self._operation == "*":
                result *= num
            elif self._operation == "/" and num != 0:
                result /= num
        return round(result, 2)
    def __str__(self):
        return f"Результат обчисленння: {self._calculate()}"
cipher = Encryptor(100, 50, 25, 1)
print(cipher)
