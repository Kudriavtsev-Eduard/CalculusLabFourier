from typing import Callable
import math


class FourierAssembler:
    def __init__(self, zero_coeff: float, cos_coeff: Callable[[int], float],
                 sin_coeff: Callable[[int], float],
                 argument_transformer: Callable[[float], float],
                 name: str = 'null'):
        self.cos_coeff = cos_coeff
        self.sin_coeff = sin_coeff
        self.zero_coeff = zero_coeff
        self.argument_transformer = argument_transformer
        self.name = name

    def get_name(self) -> str:
        return self.name

    def assemble(self, num: int) -> Callable[[float], float]:
        def result(x: float) -> float:
            nonlocal num
            res = self.zero_coeff
            for k in range(1, num + 1):
                res += (self.cos_coeff(k) * math.cos(k * self.argument_transformer(x)) +
                        self.sin_coeff(k) * math.sin(k * self.argument_transformer(x)))
            return res

        return result
