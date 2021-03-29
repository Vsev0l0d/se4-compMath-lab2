from scipy.misc import derivative

from Result import Result
from methods.Method import Method

dx = 0.00001


class SecantMethod(Method):
    name = 'Метод секущих'

    def solve(self) -> Result:
        f = self.equation.function
        pre_prev = self.choose_initial_x()
        prev = pre_prev - 0.5
        fpre_prev = f(pre_prev)
        fprev = f(prev)

        iteration = 0
        while True:
            iteration += 1
            x = prev - (prev - pre_prev)*fprev/(fprev - fpre_prev)
            fx = f(x)
            diff = abs(x - prev)
            if self.log:
                print(f'{iteration}: xk-1 = {pre_prev:.3f}, f(xk-1) = {fpre_prev:.3f}, '
                      f'xk = {prev:.3f}, f(xk) = {fprev:.3f}, '
                      f'xk+1 = {x:.3f}, f(xk+1) = {fx:.3f}, |xk - xk+1| = {diff:.3f}')
            if diff <= self.epsilon or abs(fx) <= self.epsilon:
                break
            pre_prev = prev
            prev = x
            fpre_prev = fprev
            fprev = fx

        return Result(x, fx, iteration, self.decimal_places)

    def choose_initial_x(self) -> float:
        a = self.left
        b = self.right
        f = self.equation.function
        # выбираем по условию быстрой сходимости (если получится)
        return a if f(a) * derivative(f, a, dx, 2) > 0 else b
