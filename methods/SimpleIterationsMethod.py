import numpy
from scipy.misc import derivative

from Equation import Equation
from Result import Result
from methods.Method import Method

dx = 0.00001
steps = 100


class SimpleIterationsMethod(Method):
    name = 'Метод простой итерации'

    def __init__(self, equation: Equation, left: float, right: float,
                 epsilon: float, decimal_places: int, log: bool):
        super().__init__(equation, left, right, epsilon, decimal_places, log)
        f = self.equation.function
        max_derivative = max(derivative(f, self.left, dx), derivative(f, self.right, dx))
        _lambda = - 1 / max_derivative
        self.phi = lambda x: x + _lambda * f(x)

    def check(self):
        if not self.equation.root_exists(self.left, self.right):
            return False, 'Отсутствует корень на заданном промежутке'

        # Достаточное условие сходимости метода |phi'(x)| < 1
        print('phi\'(a) = ', abs(derivative(self.phi, self.left, dx)))
        print('phi\'(b) = ', abs(derivative(self.phi, self.right, dx)))
        for x in numpy.linspace(self.left, self.right, steps, endpoint=True):
            if abs(derivative(self.phi, x, dx)) >= 1:
                return False, 'Не выполнено условие сходимости метода |phi\'(x)| < 1 на интервале'
        return True, ''

    def solve(self) -> Result:
        f = self.equation.function

        prev = self.left

        iteration = 0
        while True:
            iteration += 1
            x = self.phi(prev)

            diff = abs(x - prev)
            if self.log:
                print(f'{iteration}: xk = {prev:.3f}, f(xk) = {f(prev):.3f}, '
                      f'xk+1 = 𝜑(𝑥𝑘) = {x:.3f}, |xk - xk+1| = {diff:.3f}')

            if diff <= self.epsilon:
                break
            prev = x
        return Result(x, f(x), iteration, self.decimal_places)
