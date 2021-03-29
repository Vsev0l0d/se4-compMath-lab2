import math
from Equation import Equation
from methods.HalfDivisionMethod import HalfDivisionMethod
from methods.SecantMethod import SecantMethod
from methods.SimpleIterationsMethod import SimpleIterationsMethod

import mainboilerplate

methods = {
    1: HalfDivisionMethod,
    2: SecantMethod,
    3: SimpleIterationsMethod
}

predefined_functions = {
    # Wolfram: https://cutt.ly/hxNS7NA
    1: Equation(lambda x: (2.3 * x ** 3 + 5.75 * x ** 2 - 7.41 * x - 10.6), '2.3*x^3 + 5.75*x^2 - 7.41*x - 10.6'),
    # https://cutt.ly/6zNbCha
    2: Equation(lambda x: (x / 2 - 2 * (x + 2.39) ** (1 / 3)), 'x/2 - 2*(x + 2.39)^(1/3)'),
    # https://cutt.ly/MzNdHH5
    3: Equation(lambda x: (-x / 2 + math.e ** x + 5 * math.sin(x)), '-x/2 + e^x + 5*sin(x)')
}

ENABLE_LOGGING = True

while True:
    function = mainboilerplate.choose_equation(predefined_functions)

    method_number = mainboilerplate.choose_method_number(methods)

    while True:
        left, right, epsilon, decimal_places = mainboilerplate.read_initial_data()

        method = methods[method_number](function, left, right, epsilon, decimal_places, ENABLE_LOGGING)
        try:
            verified, reason = method.check()
        except TypeError as te:
            print('(!) Ошибка при вычислении значения функции, возможно она не определена на всем интервале.')
            continue
        if verified:
            break
        else:
            print('(!) Введенные исходные данные для метода некорректны: ', reason)

    try:
        function.draw(left, right)
    except Exception as e:
        print('(!) Не удалось построить график функции, ', e)

    output_file_name = input("Введите имя файла для вывода результата или пустую строку, чтобы вывести в консоль: ")

    try:
        if ENABLE_LOGGING:
            print('Процесс решения: ')
        result = method.solve()
    except Exception as e:
        print(e)
        print('(!) Что-то пошло не так при решении: ', e)
        continue

    mainboilerplate.print_result(result, output_file_name)

    if input('\nЕще раз? [y/n] ') != 'y':
        break
