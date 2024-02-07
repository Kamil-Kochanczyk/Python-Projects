"""
Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line.
Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.
"""

line = "this is a Python exercise"

first_chars = "".join([x[0] for x in line.split()])
last_chars = "".join([x[len(x) - 1] for x in line.split()])

assert first_chars == "tiaPe"
assert last_chars == "ssane"