

def check_str_brackets(str1: str) -> bool:
    """
    Перевіряє що у рядку дужки парні.
    Args:
        str1 (str): рядок для перевірки 

    Returns:
        bool
    """
    list1 = []
    brackets_dict = {'[': ']', '{': '}', '(': ')'}

    for el in str1:
        if el in brackets_dict.keys():
            list1.append(el)
        elif el in brackets_dict.values():
            if not list1 or brackets_dict[list1.pop()] != el:
                return False
    return not list1


# print(check_str_brackets("{}{}{}()()()[({})]")) - True
# print(check_str_brackets(" {[}{}{}()(])()[(}}")) - False
# print(check_str_brackets("фівфів0213"))

