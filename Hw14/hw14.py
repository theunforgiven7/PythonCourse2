from datetime import datetime


def sort_func_train(trains_lst: list) -> list:
    """
    Функція для сортування списку об'єктів класа Train
    Реалізує сортування  за пунктом призначення та часом
    Args:
        trains_lst (list): ваш ліст

    Returns:
        list: відсортованний ліст
    """
    return sorted(trains_lst, key=lambda t: (t.item, t.date_t))


class Train:
    """
    Клас для представлення потяга(пункт призначення, номер потягу,час відправлення )
    """
    def __init__(self, item: str, num_train: int, date_t: datetime):
        """
        Ініціалізує об'єкти класу Train
        Args:
            item (str): пункт призначення
            num_train (int): номер потягу
            date_t (datetime): час відправлення
        """
        self.item = item
        self.num_train = num_train
        if date_t < datetime.now():
            print('date_t не може бути меньшим за поточний час')
            self.date_t = datetime.now()
        else:
            self.date_t = date_t
