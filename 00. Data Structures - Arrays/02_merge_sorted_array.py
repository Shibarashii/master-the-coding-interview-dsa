from typing import List


def merge_sorted_arrays(a: List, b: List):
    merged = []
    i = j = 0

    while i < len(a) and j < len(b):  # While loop stops when either is met
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    # Since the loop stops when i has reached len(a) or j has reached len(b), we extend the list with the remaining slice.
    # Exactly one of the slices is non-empty, we append the remainder.
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged


m = merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30])
print(m)
