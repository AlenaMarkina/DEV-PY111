"""
My little Queue
"""
from typing import Any

# FIFO  первый пришел, первый ушел
# [1] -> [1, 2] -> [1, 2, 3]
# [1, 2, 3] -> [2, 3] -> [3]


class Queue:
    def __init__(self):
        """Реализации очереди с помощью python list, очередь реализует FIFO."""
        self.stack = []  # TODO инициализировать список

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self.stack.append(elem)  # TODO реализовать метод enqueue

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста
        :return: Извлеченный с начала очереди элемент.
        """
        if not self.stack:
            raise IndexError("Извлечь элемент из пустой очереди невозможно.")

        return self.stack.pop(0)  # TODO реализовать метод dequeue

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди,
                    1 - второй с начала элемент в очереди, и т.д.)
        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди
        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError("Неверный тип данных для ind: ожидается int.")

        if not 0 <= ind < len(self.stack):
            raise IndexError("Индекс вне границ очереди.")

        return self.stack[ind]  # TODO реализовать метод peek

    def clear(self) -> None:
        """ Очистка очереди."""
        self.stack.clear()  # TODO реализовать метод clear

    def __len__(self):
        """ Количество элементов в очереди."""
        return len(self.stack)  # TODO реализовать метод __len__


if __name__ == '__main__':
    queue = Queue()

    [queue.enqueue(i) for i in range(1, 10, 2)]
    print(queue.stack)
    print()

    for _ in range(7):
        queue.dequeue()
        print(queue.stack)
        print()

    # for _ in range(queue.__len__()):
    #     queue.dequeue()
    #     print(queue.stack)
    #     print()
    #
    # print(queue.peek(-5))
    #
    # queue.clear()
    # print(queue.stack)
    #
    # print(queue.__len__())
