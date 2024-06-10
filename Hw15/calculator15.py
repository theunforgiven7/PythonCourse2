class ValueZeroError(Exception):
    """
    Клас виключення класа Calculator
    Виключення "Ділення на нуль"
    """
    def __init__(self):
        """
        Метод створення об'єкта класу виключення
        "Ділення на нуль" (num2(int): 0)
        """
        self.message = 'помилка ділення на "0"'

    def __str__(self) -> str:
        """
        Рядкове представлдення об'єкта класу виключення
        return: опис виключення
        """
        return self.message


class Calculator:
    """
    Клас реалізує функції калкулятора
    """
    def __init__(self) -> None:
        """
        Ініціалізатор об'єкта класу Calculator
        """
        self.results_dict: dict = {}

    def __add__(self, num: int, num2: int) -> None:
        """
        Метод додавання
        Args:
            num (int): перше число
            num2 (int): друге число
        """
        result = num + num2
        self.results_dict[f"{num} + {num2}"] = result
        # print(self.results_dict)
        # print(type(self.results_dict))

    def subtraction(self, num: int, num2: int) -> None:
        """
        Метод віднімання
        Args:
            num (int): 1 число
            num2 (int): 2 число
        """
        result = num - num2
        self.results_dict[f"{num} - {num2}"] = result
        # print(self.results_dict)

    def division(self, num: int, num2: int) -> None:
        """
        Метод звічайного ділення
        Args:
            num (int): 1 число
            num2 (int): 2 число
        Raises:
            ValueZeroError: помилка ділення на 0
        """
        if num2 == 0:
            raise ValueZeroError()
        else:
            result = num / num2
            self.results_dict[f"{num} / {num2}"] = result
            # print(self.results_dict)

    def multiplication(self, num: int, num2: int) -> None:
        """
        Метод множення
        Args:
            num (int): 1 число
            num2 (int): 2 число
        """
        result = num * num2
        self.results_dict[f"{num} * {num2}"] = result

    def integer_division(self, num: int, num2: int) -> None:
        """
        Метод цілочисленого ділення
        Args:
            num (int): 1 число
            num2 (int): 2 число

        Raises:
            ValueZeroError: помилка ділення на 0
        """
        if num2 == 0:
            raise ValueZeroError("You can't divide by zero")
        else:
            result = num // num2
            self.results_dict[f"{num} // {num2}"] = result

    def remainder_from_division(self, num: int, num2: int) -> None:
        """
        Метод залишок від ділення
        Args:
            num (int): 1 число
            num2 (int): 2 число

        Raises:
            ValueZeroError: помилка ділення на 0
        """
        if num2 == 0:
            raise ValueZeroError("You can't divide by zero")
        else:
            result = num % num2
            self.results_dict[f"{num} % {num2}"] = result
        # print(self.results_dict)

    def exponentiation(self, num: int, num2: int) -> None:
        """
        Метод піднесення до степеня
        Args:
            num (int): 1 число
            num2 (int): 2 число (степень)
        """
        result = pow(num, num2)
        self.results_dict[f"{num} ** {num2}"] = result
        # print(self.results_dict)

    def get(self) -> dict:
        """
        Метод для отримання словника
        Returns:
            dict: словник з прикладами
        """
        return self.results_dict


a = Calculator()
a.integer_division(10, 2)
a.division(1, 12)
a.multiplication(1, 2)
a.__add__(10, 23)
a.subtraction(30, 10)
a.integer_division(15, 2)








# print(a.get())
