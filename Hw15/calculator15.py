

class Calculator:
    def __init__(self, num: int, num2: int) -> None:
        self.num = num
        self.num2 = num2
        self.results_dict: dict = {}

    def __add__(self, num: int, num2: int):
        result = num + num2
        self.results_dict[f"{num} + {num2}"] = result
        # print(self.results_dict)
        # print(type(self.results_dict))

    def subtraction(self, num: int, num2: int):
        result = num - num2
        self.results_dict[f"{num} - {num2}"] = result
        print(self.results_dict)

    def division(self, num: int, num2: int):
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")
        result = num / num2
        self.results_dict[f"{num} / {num2}"] = result
        print(self.results_dict)

    def multiplication(self, num: int, num2: int):
        result = num * num2
        self.results_dict[f"{num} * {num2}"] = result
        # print(self.results_dict)
    def get(self):
        return self.results_dict

a = Calculator(12, 0)
a.division()
# a.__add__(12,30)

# a.get()


class ValueError(Exception):
    """
    Клас виключення класа Calculator
    Виключення "Ділення на нуль"
    """
    def __init__(self, num2: int):
        """
        Метод створення об'єкта класу виключення
        "Ділення на нуль"
        Args:
            num2(int): 0
        """
        self.message = (
            f'помилка ділення на - {num2}'
            )

    def __str__(self) -> str:
        """
        Рядкове представлдення об'єкта класу виключення
        return: опис виключення
        """
        return self.message