"""
Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, które zwracają pełny string przez return.
Funkcje nie powinny pytać użytkownika o dane, tylko korzystać z argumentów.

def make_ruler(n): pass

def make_grid(rows, cols): pass
"""

def make_ruler(start, end):
    if (not isinstance(start, int)) or (not isinstance(end, int)):
        raise TypeError("Inappropriate argument type - type should be int.")
    
    if start < 0 or end < 0 or start > end:
        raise ValueError("Inappropriate argument value. Expected: start >= 0, end >= 0, start <= end.")
    
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
    unit = ("." * (end_length + 2)) + "|"

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

def make_rectangle(rows, columns):
    if (not isinstance(rows, int)) or (not isinstance(columns, int)):
        raise TypeError("Inappropriate argument type - type should be int.")

    if rows < 0 or columns < 0:
        raise ValueError("Inappropriate argument value. Expected: rows >= 0, columns >= 0.")
        
    horizontal_side = "---"
    vertical_side = "|"
    intersection = "+"
    rectangle = ""

    # +---+---+---+---+
    row1 = ((intersection + horizontal_side) * columns) + intersection

    # |   |   |   |   |
    row2 = ((vertical_side + (" " * len(horizontal_side))) * columns) + vertical_side

    # +---+---+---+---+
    # |   |   |   |   |
    row12 = row1 + "\n" + row2 + "\n"

    for i in range(rows):
        rectangle += row12
    
    rectangle += row1
    
    return rectangle

ruler = """|....|....|....|....|....|....|....|....|....|....|....|....|
0    1    2    3    4    5    6    7    8    9   10   11   12"""

rectangle = """+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+"""

assert make_ruler(0, 12) == ruler
assert make_rectangle(2, 4) == rectangle