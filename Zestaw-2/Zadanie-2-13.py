"""
Znaleźć łączną długość wyrazów w napisie line.
Wskazówka: można skorzystać z funkcji sum().
"""

line = "find the sum of lengths of words"
result = sum([len(x) for x in line.split()])

assert result == 26