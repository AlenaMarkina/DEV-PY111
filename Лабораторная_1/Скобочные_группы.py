# LIFO - последний пришел, первый ушел
# [1] -> [1, 2] -> [1, 2, 3]
# [1, 2, 3] -> [1, 2] -> [1]


def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    ...  # TODO реализовать проверку скобочной группы

    stack = []

    for i in brackets_row:
        if i == "(":
            pass
        elif i == ")":
            pass





if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False


