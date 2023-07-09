def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """

    if not isinstance(n, int):  # TODO реализовать рекурсивный алгоритм нахождения факториала
        raise TypeError('Число должно быть целым')

    if n < 0:
        raise ValueError('Число должно быть > 0')

    if n == 0:
        return 1

    return factorial_recursive(n-1) * n


print(factorial_recursive(5))
print(factorial_recursive(0))
print(factorial_recursive(1))
print(factorial_recursive(-2))
print(factorial_recursive(1.75))
