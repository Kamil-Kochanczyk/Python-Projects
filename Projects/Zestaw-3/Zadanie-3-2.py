"""
Co jest złego w kodzie:
"""

# Powinno być samo L.sort(), bez przypisania do L.
L = [3, 5, 4] ; L = L.sort()

# Po lewej stronie powinny być trzy zmienne, a nie dwie, np. x, y, z.
x, y = 1, 2, 3

# X to krotka, a krotki są niezmienne, nie można im zmieniać wartości.
X = 1, 2, 3 ; X[1] = 4

# 3 to niedozwolony indeks, dozwolone indeksy to 0, 1 oraz 2.
X = [1, 2, 3] ; X[3] = 4

# Typ string nie posiada metody append.
X = "abc" ; X.append("d")

# Brak obowiązkowych argumentów funkcji pow.
# Na przykład mogłoby być: L = list(map(lambda x: pow(x, 2), range(8)))
L = list(map(pow, range(8)))