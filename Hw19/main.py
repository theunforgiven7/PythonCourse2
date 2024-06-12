class List:
    """
    Class to delete selected elements in the list
    """
    def __init__(self, list_1: list) -> None:
        """
        initializes a new instance of the List class
        Args:
            list_1 (list): the list to be managed
        """
        self.list_1 = list_1

    def remove_elements(self, val: list) -> list:
        """
        removes selected elements from the list
        Args:
            val (list): the list of elements to be removed from the list

        Returns:
            list_1(list): the list after the specified elements have been removed
        """
        self.list_1 = [x for x in self.list_1 if x not in val]
        return self.list_1


list_1 =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4] # де видаляти
val = [1, 3] # що видаляти
# [2, 2, 4] #відповідь після видалення

a = List(list_1)

print(a.remove_elements(val))
