
from datetime import datetime


class Train:
    """
    Клас для представлення потяга (пункт призначення, номер потягу, час відправлення)
    """
    def __init__(self, item: str, num_train: int, date_t: datetime):
        """
        Ініціалізує об'єкти класу Train
        Args:
            item (str): пункт призначення
            num_train (int): номер потягу
            date_t (datetime): час відправлення
        """
        self.__item = item
        self.__num_train = num_train
        self.date_t = date_t

    @property
    def item(self) -> str:
        """Гетер для атрибуту пункт призначення"""
        return self.__item

    @item.setter
    def item(self, value: str) -> None:
        """Сетер-метод для атрибуту пункт призначення"""
        if not value:
            print("пункт призначення не може бути порожнім")
        self.__item = value

    @property
    def num_train(self) -> int:
        """Гетер-метод для атрибуту номер потягу"""
        return self.__num_train

    @num_train.setter
    def num_train(self, value: int) -> None:
        """Сетер-метод для атрибуту номер потягу"""
        if value <= 0:
            print("Номер потягу має бути додатнім числом")
        self.__num_train = value

    @property
    def date_t(self) -> datetime:
        """Гетер-метод для атрибуту 'час відправлення'"""
        return self.__date_t

    @date_t.setter
    def date_t(self, value: datetime) -> None:
        """Сетер-метод для атрибуту 'час відправлення'"""
        if value < datetime.now():
            print('date_t не може бути меншим за поточний час')
            self.__date_t = datetime.now()
        else:
            self.__date_t = value

