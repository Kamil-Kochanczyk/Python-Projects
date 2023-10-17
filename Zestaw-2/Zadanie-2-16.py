"""
W tekście znajdującym się w zmiennej line zamienić ciąg znaków "GvR" na "Guido van Rossum".
"""

line = "The creator of Python is GvR."
line = line.replace("GvR", "Guido van Rossum")

assert line == "The creator of Python is Guido van Rossum."