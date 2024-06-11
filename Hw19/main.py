class List:
    def __init__(self, list_for_search) -> None:
        self.list: list = list_for_search

    def deletter_elements(self, list_for_search: list) -> None:
        self.list = [i for i in self.list if i not in list_for_search]
        print(self.list)


list_1 =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]  # де видаляти
val = [1, 3]  # що видаляти
# [2, 2, 4]  # відповідь після видалення

a = List(list_1)
print(a.deletter_elements(val))
