"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""


import random
import string


def unique_el(S):

    # N = random.randint(0, 10)
    # for i in range(N):
    #     S = S + random.choice(string.ascii_lowercase)
    # print(S)

    S = S + 'papa'

    lst = []
    hash_S = hash(S)
    set_ = {hash_S}
    for i in range(len(S)):
        for n in range(i + 1, len(S) + 1):
            if hash(S[i:n]) in set_:
                continue
            else:
                lst.append((S[i:n]))
                set_.add(hash(S[i:n]))

    return lst, f'{len(lst)} уникальных подстрок'


print(unique_el(''))