def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if n < 0:  # TODO реализовать итеративный алгоритм нахождения факториала
        raise ValueError('Число должно быть > 0')

    if n == 0:
        return 1

    factorial = 1

    for i in range(n):
        factorial *= i+1

    return factorial


print(factorial_iterative(5))
print(factorial_iterative(0))
print(factorial_iterative(-3))
