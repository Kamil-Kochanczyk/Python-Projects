"""
Napisać program rysujący prostokąt zbudowany z małych kratek.
Należy zbudować pełny string, a potem go wypisać.
Przykładowy prostokąt składający się 2x4 pól ma postać:

+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   | 
+---+---+---+---+
"""

def make_rectangle(rows, columns):
    horizontal_side = "---"
    vertical_side = "|"
    intersection = "+"
    rectangle = ""

    for i in range(rows):
        rectangle += intersection

        for j in range(columns):
            rectangle += horizontal_side
            rectangle += intersection
        rectangle += "\n"

        rectangle += vertical_side

        for k in range(columns):
            rectangle += (" " * len(horizontal_side))
            rectangle += vertical_side
        rectangle += "\n"
    
    rectangle += intersection

    for i in range(columns):
        rectangle += horizontal_side
        rectangle += intersection
    
    return rectangle

rectangle = """+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+"""

assert make_rectangle(2, 4) == rectangle