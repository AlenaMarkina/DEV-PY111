# LIFO - последний пришел, первый ушел
# [1] -> [1, 2] -> [1, 2, 3]
# [1, 2, 3] -> [1, 2] -> [1]


def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    if not brackets_row:  # TODO реализовать проверку скобочной группы
        return True

    counter = 0

    for letter in brackets_row:
        if letter == "(":
            counter += 1
        elif letter == ")":
            if counter == 0:
                return False
            counter -= 1

    return True if counter == 0 else False


if __name__ == '__main__':
    print(check_brackets(")("))  # False
    print(check_brackets("(()"))  # False
    print(check_brackets("()()"))  # True
    print(check_brackets(""))  # True
    print(check_brackets("((()))"))  # True
    print(check_brackets("((()()))"))  # True


