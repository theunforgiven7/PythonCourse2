'''Виключення та класи виключень (помилок)'''

# from random import shuffle


class Card:
    '''Клас який реалізує методи та властивості стандартної гральної карти'''

    def __init__(self, type: str, k: str):
        '''
        Метод ініціалізації об'єкта карти
        :param type: номінал карти (туз, король, королева, валет)
        :param k: масть карти   (чірва, трефа, пік, бубна)
        '''

        # Public
        self.toolType = type
        self.kit = k
        self.score = 0

        self.SetScore()

    @property
    def toolType(self) -> str:
        '''
        Геттер метод який дозволяє подивитись
        значення прихованого(інкапсульованого) атрибута
        :return: значення атрибуту  self.__toolType
        '''
        return self.__toolType

    @toolType.setter
    def toolType(self, t: str):
        '''
        Сеттер метод
        для контрольованого та обмеженого доступу
        до зміни атрибута self.__toolType
        :param t: значення для запису в self.__toolType
        '''
        if t and type(t) is str:
            if t in ('Ace', 'King', 'Queen', 'Jack'):
                self.__toolType = t
            else:
                raise CardTypeError(t)
        else:
            raise CardTypeError(t)

    @property
    def kit(self) -> str:
        '''
        Геттер метод
        який дозволяє подивитись значення прихованого(інкапсульованого)атрибута
        :return: значення атрибуту  self.__kit
        '''
        dict_kit_pict = {
            'spades': '♠️', 'hearts': '❤️', 'diamond': '♦️', 'club': '♣️'
            }
        return dict_kit_pict.get(self.__kit)

    @kit.setter
    def kit(self, k: str):
        '''
        Сеттер метод
        для контрольованого та обмеженого доступу до зміни атрибута self.__kit
        :param t: значення для запису в self.__kit
        '''
        if k and type(k) is str:
            if k in ('spades', 'hearts', 'diamond', 'club'):
                self.__kit = k
            else:
                raise CardError(k)
        else:
            raise CardError(k)

    def SetScore(self):
        '''
        Метод для створення та визначення атрибути кількості
        поінтів кожної карти в залежності від номіналу
        '''
        if self.toolType == 'Ace':
            self.score = 11
        elif self.toolType == 'King':
            self.score = 4
        elif self.toolType == 'Queen':
            self.score = 3
        elif self.toolType == 'Jack':
            self.score = 2

    def __str__(self) -> str:
        '''
        Метод отримання актуальної інформації по поточній карті
        :return: рядкове представлення об'єкта карти
        '''
        return f'{self.toolType} {self.kit}'

    __repr__ = __str__

# 2 класи виключень


class CardTypeError(Exception):
    """
    Клас виключення класа Card
    Виключення для невизначеного НОМІНАЛУ карти
    """
    def __init__(self, t: str):
        """
        Метод створення об'єкта класу виключення
        "Номінал карти"
        Args:
            t(str): номінал карти
        """
        self.message = (
            f'помилка номіналу карти - {t} - невизначений номінал карти'
            )

    def __str__(self) -> str:
        """
        Рядкове представлдення об'єкта класу виключення
        return: опис виключення
        """
        return self.message


class CardError(Exception):
    """
    Клас виключення класа Card
    Виключення для невизначеної МАСТІ карти
    """
    def __init__(self, k: str):
        """
        Метод створення об'єкта класу виключення
        "МАсть карти"
        Args:
            k(str): масть уарти
        """
        self.message = (
            f'Була знайдена невідома карта {k}, яка порушає правила гри'
            )

    def __str__(self) -> str:
        """
        Рядкове представлдення об'єкта класу виключення
        return: опис виключення
        """
        return self.message
