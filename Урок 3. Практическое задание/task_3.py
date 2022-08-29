"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(*args):
    """
    :param args: аргументы для сравнения
    :return: возвращает сумму наибольших двух аргументов используя функцию sort()
    """
    tmp = list(args)
    tmp.sort()
    return tmp[-1] + tmp[-2]


def my_func2(a, b, c):
    """
    :param a: 1 аргумент
    :param b: 2 аргумент
    :param c: 3 аргумент
    :return: возвращает сумму наибольших двух аргументов
    """
    if a > b:
        if b > c:
            return a + b
        else:
            return a + c
    else:
        if a > c:
            return b + a
        else:
            return b + c
    return


print(my_func(9, 12, 2))
print(my_func2(2, 12, 9))
