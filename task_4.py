nums = [3, 2, 3]


def predominant_element(data: list) -> int:
    element = {}
    for i in data:
        a = data.count(i)
        print(i, a)
        element.update({i: a})

    print(element)


predominant_element(nums)
