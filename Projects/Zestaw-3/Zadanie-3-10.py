"""
Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) na liczby arabskie.
Podać kilka sposobów tworzenia takiego słownika.
Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].
"""

arabic1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

arabic2 = {}
arabic2["I"] = 1
arabic2["V"] = 5
arabic2["X"] = 10
arabic2["L"] = 50
arabic2["C"] = 100
arabic2["D"] = 500
arabic2["M"] = 1000

roman_numerals = ["I", "V", "X", "L", "C", "D", "M"]
arabic_numerals = [1, 5, 10, 50, 100, 500, 1000]
arabic3 = dict(zip(roman_numerals, arabic_numerals))

assert arabic1 == arabic2 == arabic3

def roman_to_arabic(roman):
    numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    previous = 0

    for digit in reversed(roman):
        current = numerals[digit]
        if current < previous:
            total -= current
        else:
            total += current
        previous = current
    
    return total

assert roman_to_arabic("MMMDCCXLVIII") == 3748