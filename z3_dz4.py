# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math
from math import pi

d = int(input("Введите число = "))
print(round(pi, d))
