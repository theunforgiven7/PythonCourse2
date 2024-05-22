
class MobPhone:
    """
    shows information about the phone
    """
    def __init__(self, brand: str, price: int, size_h: int, size_w: int):
        """
        Initializes a mobile phone object .
        Args:
            brand (str): Phone name
            price (int): The price of the phone
            size_h (int): Phone height
            size_w (int): The width of the phone
        """
        self.brand = brand
        self._price = price
        self._size_h = size_h
        self._size_w = size_w

    def getData(self) -> str:
        """
        all information about the phone
        Return:
            str
        """
        return (f"""Phone brand: {self.brand}
            Phone price: {self._price}
            Phone size : {self._size_h} x {self._size_w} mm.
            """)

    def get_size_h(self) -> int:
        """
        returns the height of the phone.
        Returns:
            int
        """
        return self._size_h

    def set_size_h(self, value: int) -> None:
        """
        sets the height of the phone.(The method has a condition)
        Args:
            value (int)
        """
        if value > 0:
            self._size_h = value
        else:
            print("invalid height value!")

    def get_size_w(self) -> int:
        """
        returns the width of the phone.
        Returns:
            int
        """
        return self._size_w

    def set_size_w(self, value: int) -> None:
        """
        sets the width of the phone.(The method has a condition)
        Args:
            value (int)
        """
        if value > 0:
            self._size_w = value
        else:
            print("invalid width value!")

    def get_price(self) -> int:
        """
        returns the price of the phone.
        Returns:
            int
        """
        return self._price

    def set_price(self, value: int) -> None:
        """
        returns the price of the phone(The method has a condition).
        Args:
            value (int)
        """
        if value >= 0:
            self._price = value
        else:
            print("invalid price value!")
