"""
Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?
"""

# Poniższa składnia ze średnikami jest dozwolona, ale niezalecana.
# Średniki powinny być używane tylko do oddzielania instrukcji w jednej linii.
# Na końcu linii średniki nic nie robią.
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

# Poniższa składnia jest niepoprawna.
# if nie jest instrukcją prostą i nie może być zapisana w tym samym wierszu co for.
# for i in "axby": if ord(i) < 100: print (i)

# Poniższa składnia jest poprawna.
for i in "axby": print(ord(i) if ord(i) < 100 else i)