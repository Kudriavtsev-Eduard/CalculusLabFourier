import numpy as np
from typing import Callable

from matplotlib import pyplot as plt
from src.fourier_assembler import FourierAssembler


class FourierVisualizer:
    def __init__(self, function: Callable[[float], float], assembler: FourierAssembler,
                 boundary: tuple[float, float]) -> None:
        self.function = function
        self.assembler = assembler
        self.boundary = boundary

    @staticmethod
    def visualize_graph(func: Callable[[float], float], x, title: str = 'null') -> None:
        y = np.vectorize(func)(x)
        plt.plot(x, y, label=title)

    def visualize(self, *sum_numbers: int) -> None:
        sum_numbers_no_duplicates = sorted(set(sum_numbers))
        begin = self.boundary[0]
        end = self.boundary[1]
        x = np.linspace(begin, end, 1000)
        self.visualize_graph(self.function, x, 'graph')
        for num in sum_numbers_no_duplicates:
            self.visualize_graph(self.assembler.assemble(num), x, f'S_{num}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.legend()
        plt.title(self.assembler.get_name())
        plt.show()
