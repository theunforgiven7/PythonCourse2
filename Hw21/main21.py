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
            
# a = Potion([1,24, 23], 2)

