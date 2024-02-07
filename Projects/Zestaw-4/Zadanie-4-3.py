"""
Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.
"""

def factorial_recur(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recur(n - 1)

def factorial_iter(n):
    if not isinstance(n, int):
        raise TypeError("Inappropriate argument type - type should be int.")
    
    if n < 0:
        raise ValueError("Inappropriate argument value. Expected: n >= 0")
    
    factorial = 1

    for i in range(2, n + 1):
        factorial *= i
    
    return factorial

for i in range(11):
    assert factorial_iter(i) == factorial_recur(i)