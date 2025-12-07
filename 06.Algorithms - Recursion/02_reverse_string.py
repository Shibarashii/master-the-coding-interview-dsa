def reverse_iterative(s):
    reversed_s = []
    for i in range(len(s)-1, -1, -1):
        reversed_s.append(s[i])
    return "".join(reversed_s)


def reverse_recursive(s):
    if len(s) <= 0:
        return s
    return reverse_recursive(s[1:]) + s[0]


print(reverse_iterative("Hello"))
print(reverse_recursive("Hello"))
