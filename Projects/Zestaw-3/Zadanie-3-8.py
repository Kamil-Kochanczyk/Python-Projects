"""
Dla dwóch sekwencji liczb lub znaków znaleźć:
(a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń),
(b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).
"""

A = [-10, -10, -10, -8, 0, 8, 10, 10, 10]
B = [10, 3, 1, 0, 0, 0, -1, -3, -10]

intersection = list(set(A) & set(B))
assert sorted(intersection) == [-10, 0, 10]

sum = list(set(A) | set(B))
assert sorted(sum) == [-10, -8, -3, -1, 0, 1, 3, 8, 10]