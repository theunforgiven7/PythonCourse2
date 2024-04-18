"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
"""

def move_zeros_to_end(lst: list)->list:
    """
    func moves all of the zeros to the end, preserving the order of the other elements.
    Args:
        lst (list): list with zero/zeros

    Returns:
        list: with zeros at the end of the list
    """
    return [i for i in lst if i != 0 or i is False] + [i for i in lst if i == 0 and i is not False]

# print(move_zeros_to_end([False,1,0,1,2,0,1,3,"a"]))
# print(move_zeros_to_end([0, False]))
