import json
from calculator15 import Calculator, a


class FileNotFoundError(Exception):
    """
    Клас виключення класа File_maker
    """
    def __init__(self, filename: str) -> None:
        """
        Метод створення об'єкта класу виключення
        """
        self.message = f'Файл не знайдено - {filename}'

    def __str__(self) -> str:
        """
        Рядкове представлдення об'єкта класу виключення
        return: опис виключення
        """
        return self.message


class File_maker:
    """
    Клас для роботи з файлами у форматі JSON
    дозволяє зберігати словники даних у файл та завантажувати дані з файлу
    """
    def __init__(self, filename: str) -> None:
        """
        Ініціалізатор об'єкта класу File_maker
        Args:
            filename (str): назва файлу для збереження або завантаження даних
        """
        self.filename = filename

    def save_dict(self, dict1: dict) -> None:
        """
        Зберігає словник у файл у форматі JSON
        Args:
            dict1 (dict)
        """
        with open(self.filename, 'w') as f:
            json.dump(dict1, f, indent=4, ensure_ascii=False)

    def load_dict(self) -> dict:
        """
        Завантажує дані з файлу у вигляді словника
        Returns:
            dict
        """
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Файл {self.filename} не знайдено.")
            return {}

    def sum_of_first_five(self):
        """
        Обчислює суму перших п'яти значень у dict, завантаженому з файлу
        Returns:
            int or float:  Сума перших п'яти значень, інакше повертає 0
        """
        dict1 = self.load_dict()
        if len(dict1) < 5:
            print("У файлі менше п'яти записів(прикладів).")
            return 0
        else:
            return sum(list(dict1.values())[:5])


file_task = File_maker('result.json')
file_task.save_dict(a.get())
loaded_dict = file_task.load_dict()
print(loaded_dict)

sum_result = file_task.sum_of_first_five()
print("Сума перших 5 результатів:", sum_result)
