"""
Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3.
"""

numbers = []
for i in range(31):
    if i % 3 != 0:
        numbers.append(i)

assert numbers == [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29]