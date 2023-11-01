"""
Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która może zawierać zagnieżdżone podsekwencje.
Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).
"""

def sum_seq(sequence):
    sum = 0
    for i in range(len(sequence)):
        if isinstance(sequence[i], (list, tuple)):
            sum += sum_seq(sequence[i])
        else:
            sum += sequence[i]
    return sum

sequence = [(1, [3, 5], 8), 10, -1, [4, 7, (-11, 13)]]
assert sum_seq(sequence) == 39

sequence = (-10, 8, (1, 1, 1), [2, 6, (-1, -4, -7, [0, 1, 2])], 3)
assert sum_seq(sequence) == 3