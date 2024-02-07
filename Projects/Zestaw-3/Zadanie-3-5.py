"""
Napisać program rysujący "miarkę" o zadanej długości.
Należy prawidłowo obsłużyć liczby składające się z kilku cyfr (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej).
Należy zbudować pełny string, a potem go wypisać.

|....|....|....|....|....|....|....|....|....|....|....|....|
0    1    2    3    4    5    6    7    8    9   10   11   12
"""

def make_ruler(start, end):
    # Assuming that start and end are natural numbers and that start <= end
    # In this case length will also be a natural number
    length = end - start

    # Finding the number of digits of start
    start_length = len(str(start))

    # Finding the number of digits of end
    end_length = len(str(end))

    # Starting to create the top of the ruler
    # We have to correctly position the first vertical bar above the last digit of the first number
    top = f"{"|":>{start_length}}"

    # We have to include enough dots between vertical bars
    # This way the numbers will not be too close to each other
    # We take into consideration the biggest number that we want to print
    unit = ("." * (end_length + 3)) + "|"

    # Finishing the top of the ruler
    top += (unit * length) + "\n"

    # Creating the bottom of the ruler
    # We will put each substring into a list and then join all substrings at the end
    bottom = [str(start)]
    for i in range(start + 1, end + 1):
        bottom.append(f"{i:>{len(unit)}}")
    bottom = "".join(bottom)

    # Finishing the ruler
    ruler = top + bottom

    return ruler

ruler = """|.....|.....|.....|.....|.....|.....|.....|.....|.....|.....|.....|.....|
0     1     2     3     4     5     6     7     8     9    10    11    12"""

assert make_ruler(0, 12) == ruler

ruler = """   |........|........|........|........|........|........|........|........|........|........|
9995     9996     9997     9998     9999    10000    10001    10002    10003    10004    10005"""

assert make_ruler(9995, 10005) == ruler