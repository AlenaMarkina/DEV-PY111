from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    # TODO реализовать алгоритм сортировки подсчетами
    if not container or len(container) == 1:
        return container

    max_in_container = container[0]

    # Находим максимальный элемент в массиве.
    for i in container:
        if i > max_in_container:
            max_in_container = i

    # Создаем вспомогательный массив.
    count = [0 for _ in range(max_in_container+1)]

    # Заполняем вспомогательный массив.
    for i in container:
        count[i] += 1

    new_str = ''

    # Рапаковываем вспомогательный массив в строку.
    # i - цифра, count[i] - сколько раз цифра встречается в неотсортированном массиве
    for i in range(len(count)):
        if count[i] > 0:
            # print(f'цифра {i} встречается {count[i]} раз')
            new_str += (str(i) + ' ') * count[i]

    # print(new_str)  # '1 3 3 3 4 14 22'
    new_str = new_str.split(' ')
    container_sorted = [int(i) for i in new_str[:-1]]  # Не берем последний элемент, тк это пробел.

    return container_sorted


a1 = [1, 0, 2, 3, 3, 0, 7, 11, 1, 100, 100]
a2 = [1, 2, 3, 4]
a3 = [101]
a4 = []

print(sort(a1))
print(sort(a2))
print(sort(a3))
print(sort(a4))
