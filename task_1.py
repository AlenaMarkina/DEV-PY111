s = "anagram"
t = "nagaram"


def is_anagram(str_1, str_2):
    str_1 = list(str_1)
    str_2 = list(str_2)
    str_1.sort()
    str_2.sort()

    idx = 0

    while idx < len(str_1):

        if str_1[idx] == str_2[idx]:
            idx += 1
        else:
            return False
    return True




print(is_anagram(s, t))




