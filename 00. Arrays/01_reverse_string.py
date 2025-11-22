def reverse_string(string: str) -> str:
    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]

    return reversed_string


a = reverse_string("hello")
print(a)
