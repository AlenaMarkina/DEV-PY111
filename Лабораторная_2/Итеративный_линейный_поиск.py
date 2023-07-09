"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """

    if arr:  # TODO реализовать итеративный линейный поиск

        min_value = arr[0]
        idx = 0

        for i in range(len(arr)):
            if arr[i] < min_value:
                min_value = arr[i]
                idx = i

        return idx
    else:
        raise ValueError('Пустая последовательность')


arr1 = [2, 3, 0, 4, -1, 5, 10, -1]
arr2 = [-1, -1, 0, 4, -1, 5, 10, -1]
arr3 = [12]
arr4 = []

print(min_search(arr1))
print(min_search(arr2))
print(min_search(arr3))
print(min_search(arr4))
