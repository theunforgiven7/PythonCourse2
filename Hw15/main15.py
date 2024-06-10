import json
from calculator15 import Calculator, a


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
        with open(self.filename, 'r') as f:
            return json.load(f)

    def sum_of_first_five_num(self):
        """
        Обчислює суму перших п'яти значень у dict, завантаженому з файлу
        Returns:
            int or float:  Сумy перших п'яти значень, інакше повертає 0
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

sum_result = file_task.sum_of_first_five_num()
print("Сума перших 5 результатів:", sum_result)
