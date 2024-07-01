class ColorError(Exception):
    """
    Клас виключення для Potion
    """
    def __init__(self, color: list) -> None:
        """
        Метод створення об'єкта класу виключення "Помилка списка color"
        Args:
            color (list): поточний список
        """
        self.message = f'''За умовою список color повинен містити числа,
            які можуть бути тільки цілими і в діапазоні від 0 до 255 включно.
            Зафіксовано: {color} '''

    def __str__(self) -> str:
        '''
        Рядкове представлдення об'єкта класу виключення
        :return: опис виключення
        '''
        return self.message


class VolumeError(Exception):
    """Клас виключення для Potion"""
    def __init__(self, volume: int) -> None:
        """
        Метод створення об'єкта класу виключення "Помилка volume"
        Args:
            volume(int): об'єм
        """
        self.message = f'''За умовою volume
        може бути тільки цілим невід'ємним числом. Зафіксовано: {volume} '''

    def __str__(self) -> str:
        '''
        Рядкове представлдення об'єкта класу виключення
        :return: опис виключення
        '''
        return self.message


class MixFuncError(Exception):
    """Клас виключення для Potion"""
    def __init__(self) -> None:
        """
        Метод створення об'єкта класу виключення "Помилка іншого Potion об'єкта"
        """
        self.message = '''Аргумент повинен бути об'єктом класу Potion. '''

    def __str__(self) -> str:
        '''
        Рядкове представлдення об'єкта класу виключення
        :return: опис виключення
        '''
        return self.message


class Potion:
    """
    Клас для представлення зілля
    """
    def __init__(self, color: list, volume: int) -> None:
        """
        Ініціалізує об'єкт зілля з заданими параметрами кольору та об'єму
        Args:
            color (list): список інтенсивності кольорів RGB
            volume (int): число яке позначає об'єм в умовних магічних одиницях
        """
        def __init__(self, color: list, volume: int):
            self.color = color
            self.volume = volume

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value: list):
        if not isinstance(value, list) or len(value) != 3:
            raise ColorError(value)
        for i in value:
            if not isinstance(i, int) or i < 0 or i > 255:
                raise ColorError(value)
        self._color = value

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise VolumeError(value)
        self._volume = value

    def mix(self, other: 'Potion') -> 'Potion':
        """
        Метод для змішування поточного зілля з іншим зіллям(того ж классу)
        та повертає нове змішане зілля
        Args:
            other (Potion): Інший об'єкт класу Potion,
            з яким потрібно змішати зілля
        Returns:
            Potion: Новий об'єкт класу Potion, що представляє змішане зілля
        """
        if not isinstance(other, Potion):
            raise MixFuncError()
        new_potion_value = self.volume + other.volume
        new_potion_color = [(
            self.color[el] * self.volume + other.color[el] * other.volume) // new_potion_value
                            for el in range(3)]

        return Potion(new_potion_color, new_potion_value)


potio_piperis = Potion([255, 255, 255], 7)
potio_developing = Potion([51, 102, 51], 12)
new_potion = potio_piperis.mix(potio_developing)

print(new_potion.color)
print(new_potion.volume)
