"""
Mamy dany napis wielowierszowy line.
Podać sposób obliczenia liczby wyrazów w napisie.
Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami (spacja, tabulacja, newline).
"""

line = """This is a multi-line string.
It can be created - for example - with triple quotes."""
number_of_words = len(line.split())

assert number_of_words == 16