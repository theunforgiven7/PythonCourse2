class Potion:
    def __init__(self, color: list, volume: int):
        if not isinstance(color, list) or len(color) != 3:
            raise ValueError('color error')
        for i in color:
            if not isinstance(i, int) or i < 0 or i > 255:
                raise ValueError('error1')
        self.color = color

        if not isinstance(volume, int) or volume < 0:
            raise ValueError('value error')
        self.volume = volume
            
    def mix(self, other):
        if not isinstance(other, Potion):
            raise ValueError('error class')
        new_potion_value = self.volume + other.volume
        new_potion_color = [(
            self.color[el] + other.color[el]) // len(self.color) + len(other.color)
                            for el in range(3)]

        return Potion(new_potion_color, new_potion_value)


potio_piperis = Potion([255, 255, 255], 7)
potio_developing = Potion([51, 102, 51], 12)
new_potion = potio_piperis.mix(potio_developing)

print(new_potion.color)
print(new_potion.volume)

