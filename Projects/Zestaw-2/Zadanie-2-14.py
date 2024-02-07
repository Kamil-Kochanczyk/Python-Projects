"""
Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line.
"""

line = "literally literal unnatural unnaturally"
words = line.split()
lengths = [len(x) for x in words]
longest_word_length = max(lengths)
longest_word = words[lengths.index(longest_word_length)]

assert longest_word_length == 11
assert longest_word == "unnaturally"