"""
Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości.
Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji.
Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(seq))   # [1,2,3,4,5,6,7,8,9]
"""

def flatten(sequence):
    flat_seq = []

    for i in range(len(sequence)):
        if isinstance(sequence[i], (list, tuple)):
            flat_subseq = flatten(sequence[i])
            for i in range(len(flat_subseq)):
                flat_seq.append(flat_subseq[i])
        else:
            flat_seq.append(sequence[i])
    
    return flat_seq if isinstance(sequence, list) else tuple(flat_seq)

sequence = [[1, (2, 3)], ([], [4, (5, 6, 7)]), (8, [9])]
assert flatten(sequence) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

sequence = ([([1, 3], 5), 2, 4], (7, -4), 11, [-1, -2, -3], [[[[]]]], (((0))))
assert flatten(sequence) == (1, 3, 5, 2, 4, 7, -4, 11, -1, -2, -3, 0)