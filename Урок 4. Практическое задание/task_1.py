"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv
script_name, working_time, rate, bonus = argv


def get_salary(working_time, rate, bonus):
    return (int(working_time) * int(rate)) + int(bonus)


print(get_salary(working_time, rate, bonus))
