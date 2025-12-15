def factorial_recursive(x):
    if x == 0:
        return 1
    return x * factorial_recursive(x-1)


def factorial_iterative(x):
    total = 1
    for i in range(x, 0, -1):
        total *= i
    return total


print(factorial_recursive(5))
print(factorial_iterative(5))
