"""
Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie.
Chcemy zbudować napis z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024.
Wskazówka: str.zfill().
"""

L = [4, 7, 11, 13, 100, 999]
s = " ".join([str(x).zfill(3) for x in L])

assert s == "004 007 011 013 100 999"