"""
Stworzyć plik fracs.py i zapisać w nim funkcje do działań na ułamkach.
Ułamek będzie reprezentowany przez listę dwóch liczb całkowitych [licznik, mianownik].
Napisać kod testujący moduł fracs.
Nie należy korzystać z klasy Fraction z modułu fractions.
Można wykorzystać funkcję fractions.gcd() implementującą algorytm Euklidesa.
"""

import fractions

def canonical_form(frac):
    """
    Converts a fraction to its canonical form.
    In canonical form numerator is either positive or negative and denumerator is always positive.
    """
    num, denum = frac
    num = int(fractions.math.fabs(num))
    denum = int(fractions.math.fabs(denum))
    if not is_positive(frac):
        num *= -1
    return [num, denum]

def simplify_frac(frac):
    num, denum = frac
    gcd = fractions.math.gcd(num, denum)
    return canonical_form([num // gcd, denum // gcd])

def add_frac(frac1, frac2):
    if is_undefined(frac1) or is_undefined(frac2):
        raise ValueError("Value error: fraction is undefined.")
    num1, denum1 = canonical_form(frac1)
    num2, denum2 = canonical_form(frac2)
    denum = fractions.math.lcm(denum1, denum2)
    num = (num1 * (denum // denum1)) + (num2 * (denum // denum2))
    return simplify_frac([num, denum])

def sub_frac(frac1, frac2):
    num2, denum2 = frac2
    return add_frac(frac1, [-num2, denum2])

def mul_frac(frac1, frac2):
    if is_undefined(frac1) or is_undefined(frac2):
        raise ValueError("Value error: fraction is undefined.")
    num1, denum1 = frac1
    num2, denum2 = frac2
    return simplify_frac([num1 * num2, denum1 * denum2])

def div_frac(frac1, frac2):
    if is_undefined(frac1) or is_undefined(frac2):
        raise ValueError("Value error: fraction is undefined.")
    if is_zero(frac2):
        raise ZeroDivisionError("Denominator is zero.")
    num2, denum2 = frac2
    return mul_frac(frac1, [denum2, num2])

def is_positive(frac):
    num, denum = frac
    return num * denum > 0

def is_zero(frac):
    num = frac[0]
    return (num == 0) and (not is_undefined(frac))

def is_undefined(frac):
    denum = frac[1]
    return denum == 0

def cmp_frac(frac1, frac2):
    if is_undefined(frac1) or is_undefined(frac2):
        raise ValueError("Value error: fraction is undefined.")
    
    result = None

    if simplify_frac(frac1) == simplify_frac(frac2):
        result = 0
    else:
        num1, denum1 = canonical_form(frac1)
        num2, denum2 = canonical_form(frac2)
        common_denum = fractions.math.lcm(denum1, denum2)
        num1 *= (common_denum // denum1)
        num2 *= (common_denum // denum2)
        result = -1 if num1 < num2 else 1
    
    return result

def frac2float(frac):
    if is_undefined(frac):
        raise ValueError("Value error: fraction is undefined.")
    num, denum = frac
    return num / denum
