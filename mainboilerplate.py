from typing import Tuple

from Equation import Equation
import decimal


def choose_equation(functions) -> Equation:
    print("Выберите уравнение:")
    for num, func in functions.items():
        print(str(num) + ': ' + func.text)
    try:
        equation_number = int(input("Введите номер уравнения: "))
    except ValueError:
        print('(!) Вы ввели не число')
        return choose_equation(functions)
    if equation_number < 1 or equation_number > len(functions):
        print("(!) Такого номера нет.")
        return choose_equation(functions)
    return functions[equation_number]


def choose_method_number(methods) -> int:
    print("Выберите метод:")
    for num, mtd in methods.items():
        print(str(num) + ': ' + mtd.name)
    try:
        method_number = int(input("Введите номер метода: "))
    except ValueError:
        print('(!) Вы ввели не число')
        return choose_method_number(methods)
    if method_number < 1 or method_number > len(methods):
        print("(!) Такого номера нет.")
        return choose_method_number(methods)
    return method_number


def print_result(result, output_file_name):
    if output_file_name == '':
        print('\n' + str(result))
    else:
        f = open(output_file_name, "w")
        f.write(str(result))
        f.close()
        print('Результат записан в файл.')


def read_initial_data() -> Tuple[float, float, float, int]:
    while True:
        filename = input("Введите имя файла для загрузки исходных данных и интервала "
                         "или пустую строку, чтобы ввести вручную: ")
        if filename == '':
            left = float(input('Введите левую границу интервала: '))
            right = float(input('Введите правую границу интервала: '))
            epsilon = input('Введите погрешность вычисления: ')
            break
        else:
            try:
                f = open(filename, "r")
                left = float(f.readline())
                right = float(f.readline())
                epsilon = f.readline()
                f.close()
                print('Считано из файла:')
                print(f'Левая граница: {left}, правая: {right}, погрешность: {epsilon}')
                break
            except FileNotFoundError:
                print('(!) Файл для загрузки исходных данных не найден.')

    decimal_places = abs(decimal.Decimal(epsilon).as_tuple().exponent)
    epsilon = float(epsilon)

    return left, right, epsilon, decimal_places
