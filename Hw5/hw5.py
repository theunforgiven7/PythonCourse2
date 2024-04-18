"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
"""

def move_zeros_to_end(lst: list)->list:
    """
    func moves all of the zeros to the end, preserving the order of the other elements.
    Args:
        lst (list): list with zero 

    Returns:
        list: with zeros at the end of the list
    """
    for element in lst: 
        if element == 0:
            lst.remove(element)
            lst.append(element)
    return lst


# print(move_zeros_to_end([1,2,0,1,0,1,0,3,0,1]))
# print(move_zeros_to_end([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))
# print(move_zeros_to_end(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]))
# print(move_zeros_to_end(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))
# print(move_zeros_to_end([0,1,None,2,False,1,0]))
# print(move_zeros_to_end(["a","b"]))
# print(move_zeros_to_end(["a"]))
# print(move_zeros_to_end([0, 0, 1]))
# print(move_zeros_to_end([0]))
# print(move_zeros_to_end([False]))
# print(move_zeros_to_end([]))


