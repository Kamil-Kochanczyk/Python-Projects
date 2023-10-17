"""
Na liście L znajdują się liczby całkowite dodatnie.
Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.
"""

L = [520, 1085, 321, 713]
s = "".join([str(x) for x in L])

assert s == "5201085321713"