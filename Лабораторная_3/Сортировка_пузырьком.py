from typing import Sequence


def sort(arr: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param arr: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    counter = len(arr) - 1  # TODO реализовать алгоритм сортировки пузырьком
    flag = 0  # Исходный массив не отсортирован

    while counter >= 1:

        for i in range(counter):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i+1], arr[i]
            else:
                flag += 1

        if flag == counter:
            return arr

        counter -= 1

    return arr


a1 = [-100, 4, 3, 2, 1, 0, -3]
a2 = [2]
a3 = []
a4 = [1, 2, 3, 4]

print(sort(a1))
print(sort(a2))
print(sort(a3))
print(sort(a4))
