
"""Task 1"""


#list1 = [1, 10, 4, 13, 22, 10, 0 , 105, 12, 11, 105]


def return_max(list1: list)->int:
    """
    Args:
        list1 (list): list of numbers(type int)

    Returns:
        int: returns the largest even number from the list
    """
    mux = max([mux for mux in list1 if mux % 2 == 0])
    return mux


print(return_max(list1=))




"""Task 2"""

# list2 = [1, 10, 4, 13, 22, 10, 0 , 105, 12, 11, 105]
#  max_1 = 105, max_2 = 22. max_3 == 13 


def return_max_3(list2: list)->tuple:
    """“Finding the 3 maximum numbers in the list
    Args:
        list2 (list): list of numbers
    Returns:
        tuple: 3 maximum numbers
    """
    num_sorted = list(set(list2))
    num_sorted.sort(reverse=True)
    return num_sorted[0], num_sorted[1], num_sorted[2]


print(return_max_3(list2=))

"""Task 3"""

def lists_even_odd(list1: list , list2: list)-> bool:
    """
    Функція порівнює кількість парних чисел в першому списку з кількістю непарних чисел в другому списку.

    Параметри:
    list1 (list): Перший список (int).
    list2 (list): Другий список (int).

    Повертає:
    bool: Повертає True, якщо кіл-ть парних чисел в першому списку більша за кіл-ть непарних чисел в другому списку. В іншому випадку повертає False.
    """
    even_nums = [num for num in list1 if num % 2 == 0]
    
    odd_nums = [num for num in list2 if num % 2 != 0]
    
    return len(even_nums) > len(odd_nums)

# print(lists_even_odd([1, 10, 4, 13, 22, 10, 0 , 100, 12, 14, 105],  [1, 1, 3, 13, 22, 5 , 17]))

