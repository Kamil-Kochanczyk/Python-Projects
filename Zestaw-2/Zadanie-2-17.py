"""
Posortować wyrazy z napisu line raz alfabetycznie, a raz pod względem długości.
Wskazówka: funkcja wbudowana sorted().
"""

line = "sorting words alphabetically and by length"
words = line.split()
sorted_alphabetically = sorted(words, key=str.lower)
sorted_by_length = sorted(words, key=len)

assert sorted_alphabetically == ["alphabetically", "and", "by", "length", "sorting", "words"]
assert sorted_by_length == ["by", "and", "words", "length", "sorting", "alphabetically"]