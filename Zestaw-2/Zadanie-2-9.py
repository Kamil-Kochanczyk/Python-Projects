"""
Napisać funkcję wykonującą kopiowanie pliku, która pomija linie rozpoczynające się od znaku # (linie z komentarzami).
"""

def copy_without_comments(original_filepath, copy_filepath):
    original = open(original_filepath, "r")
    copy = open(copy_filepath, "w")
    for line in original:
        if line[0] != "#":
            copy.write(line)
    original.close()
    copy.close()

o = "C:\\Users\\kocha\\Desktop\\original.txt"
c = "C:\\Users\\kocha\\Desktop\\copy.txt"
copy_without_comments(o, c)