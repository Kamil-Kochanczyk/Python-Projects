"""
Znaleźć liczbę cyfr zero w dużej liczbie całkowitej.
Wskazówka: zamienić liczbę na napis.
"""

big_number = 10200300040000
char_array = list(str(big_number))
number_of_zeros = len(list(filter(lambda x: x == "0", char_array)))

assert number_of_zeros == 10