"""
Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie.
Lista jest modyfikowana w miejscu (in place).
Rozważyć wersję iteracyjną i rekurencyjną.
"""

def reverse_iter(L, left, right):
    if (not isinstance(left, int)) or (not isinstance(right, int)):
        raise TypeError("Inappropriate argument type - left and right should be ints.")
    
    if len(L) == 0:
        raise ValueError("Inappropriate argument value - L is empty.")
    
    if (left not in range(len(L))) or (right not in range(len(L))):
        raise ValueError("Inappropriate argument value - left or right is an index out of range.")
    
    if left > right:
        raise ValueError("Inappropriate argument value. Expected: left <= right.")

    range_len = right - left + 1
    range_half = range_len // 2

    for i in range(range_half):
        L[left + i], L[right - i] = L[right - i], L[left + i]

def reverse_recur(L, left, right):    
    range_len = right - left + 1
    if range_len > 1:
        L[left], L[right] = L[right], L[left]
        reverse_recur(L, left + 1, right - 1)

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
LL = list(L)

reverse_iter(L, 3, 9)
assert L == [0, 1, 2, 9, 8, 7, 6, 5, 4, 3, 10, 11, 12, 13, 14, 15]

reverse_recur(LL, 6, 10)
assert LL == [0, 1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 11, 12, 13, 14, 15]