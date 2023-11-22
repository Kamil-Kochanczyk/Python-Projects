"""
Stworzyć następujące iteratory nieskończone:
(a) zwracający 0, 1, 0, 1, 0, 1, ...,
(b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D],
(c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia].
"""

import itertools
import random

iter_01 = itertools.cycle([0, 1])
iter_NESW = iter(lambda: random.choice(["N", "E", "S", "W"]), "")
iter_week = itertools.cycle([0, 1, 2, 3, 4, 5, 6])

list_01 = [next(iter_01) for i in range(6)]
list_NESW = [next(iter_NESW) for i in range (8)]
list_week = [next(iter_week) for i in range(15)]

assert list_01 == [0, 1, 0, 1, 0, 1]
print(list_NESW)
assert list_week == [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0]