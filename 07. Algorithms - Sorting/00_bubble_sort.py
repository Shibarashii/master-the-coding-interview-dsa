def bubble_sort(s: list):
    lens = len(s)
    for i in range(lens):
        swapped = False
        for j in range(lens - 1 - i):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]
                swapped = True
        if not swapped:
            break
    return s


sample = [3, 1, 9, 4, 5, 8, 2]
print(sample)
bubble_sort(sample)
print(sample)
