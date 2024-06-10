class ValueZeroError(Exception):
    """
    Клас виключення класа Calculator
    Виключення "Ділення на нуль"
    """
    def __init__(self):
        """
        Метод створення об'єкта класу виключення
        "Ділення на нуль"
        Args:
            num2(int): 0
        """
        self.message = (f'помилка ділення на "0"')

    def __str__(self) -> str:
        """
        Рядкове представлдення об'єкта класу виключення
        return: опис виключення
        """
        return self.message


class Calculator:
    def __init__(self) -> None:
        self.results_dict: dict = {}

    def __add__(self, num: int, num2: int) -> None:
        result = num + num2
        self.results_dict[f"{num} + {num2}"] = result
        # print(self.results_dict)
        # print(type(self.results_dict))

    def subtraction(self, num: int, num2: int):
        result = num - num2
        self.results_dict[f"{num} - {num2}"] = result
        # print(self.results_dict)

    def division(self, num: int, num2: int) -> None:
        if num2 == 0:
            raise ValueZeroError("You can't divide by zero")
        else:
            result = num / num2
            self.results_dict[f"{num} / {num2}"] = result
            # print(self.results_dict)

    def multiplication(self, num: int, num2: int) -> None:
        result = num * num2
        self.results_dict[f"{num} * {num2}"] = result

    def integer_division(self, num: int, num2: int) -> None:
        if num2 == 0:
            raise ValueZeroError("You can't divide by zero")
        else:
            result = num // num2
            self.results_dict[f"{num} // {num2}"] = result

    def remainder_from_division(self, num: int, num2: int) -> None:
        if num2 == 0:
            raise ValueZeroError("You can't divide by zero")
        else:
            result = num % num2
            self.results_dict[f"{num} % {num2}"] = result
        # print(self.results_dict)

    def exponentiation(self, num: int, num2: int) -> None:
        result = pow(num, num2)
        self.results_dict[f"{num} ** {num2}"] = result
        # print(self.results_dict)

    def get(self) -> dict:
        return self.results_dict


a = Calculator()
a.division(12, 9)
a.division(12, 9)
a.__add__(12,30)

print(a.get())
