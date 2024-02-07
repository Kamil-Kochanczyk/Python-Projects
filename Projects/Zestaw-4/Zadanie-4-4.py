"""
Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.
"""

def fibonacci_recur(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)

def fibonacci_iter(n):
    if not isinstance(n, int):
        raise TypeError("Inappropriate argument type - type should be int.")
    
    if n < 0:
        raise ValueError("Inappropriate argument value. Expected: n >= 0")
    
    result = None

    if n == 0 or n == 1:
        result = n
    else:
        minus_two = 0
        minus_one = 1

        for i in range(2, n + 1):
            result = minus_two + minus_one
            minus_two = minus_one
            minus_one = result
    
    return result

for i in range(21):
    assert fibonacci_iter(i) == fibonacci_recur(i)