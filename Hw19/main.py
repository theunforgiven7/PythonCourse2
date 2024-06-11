class List:
    """
    Class to delete selected elements in the list
    """
    def __init__(self, list1: list) -> None:
        """
        Initializes the List object
        Args:
            list_for_remove (list): the initial list
        """
        self.list: list = list1

    def deletter_elements(self, list_for_remove: list) -> None:
        """
        Removes selected elements from the list
        Args:
            list_for_remove (list): the list of elements to remove
        Return:
            list(list): Sorted list
        """
        self.list = [el for el in self.list if el not in list_for_remove]
        return (self.list)


list_1 =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]  # де видаляти
val = [1, 3]  # що видаляти
# [2, 2, 4]  # відповідь після видалення

a = List(list_1)
print(a.deletter_elements(val))
