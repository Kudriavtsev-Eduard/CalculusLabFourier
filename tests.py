from math import pi, sin, cos

from src.visualizer import FourierVisualizer
from src.fourier_assembler import FourierAssembler

general = FourierAssembler(1 / 4,
                           lambda k: 3 * (1 - (-1) ** k) / (pi ** 2 * k ** 2),
                           lambda k: ((-1) ** (k + 1) - 2) / (pi * k),
                           lambda x: pi * (x - 1),
                           'Общий тригонометрический'
                           )
cosinus = FourierAssembler(1 / 4,
                           lambda k: (pi * k * sin(pi * k / 2) + 3 * cos(pi * k / 2) - 3) * 4 / (pi ** 2 * k ** 2),
                           lambda k: 0,
                           lambda x: pi / 2 * x,
                           "По косинусам"
                           )

sinus = FourierAssembler(0,
                         lambda k: 0,
                         lambda k: (6 * sin(pi * k / 2) - pi * k - 2 * pi * k * cos(pi * k / 2)) * 2 / (
                                 pi ** 2 * k ** 2),
                         lambda x: pi / 2 * x,
                         "По синусам")


def func(x: float) -> float:
    return 3 * x - 1 if 0 <= x < 1 else 0


boundary = (0, 2)


def visualize_test(assembler: FourierAssembler):
    FourierVisualizer(func, assembler, boundary).visualize(*PARTIAL_SUMS)


PARTIAL_SUMS = (1, 5, 10, 30, 70)


def main():
    visualize_test(general)
    visualize_test(cosinus)
    visualize_test(sinus)


if __name__ == '__main__':
    main()
