"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""

a = float(input('Введите первое число:'))
b = float(input('Введите второе число:'))


def get_quotient(dividend, divider):
    """
    :param dividend: делимое
    :param divider: делитель
    :return: частное = a / b
    """
    try:
        return dividend / divider
    except ZeroDivisionError:
        print("Вы что? Пытаетесь делить на 0!")


print(get_quotient(a, b))
