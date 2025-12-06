def fibonacci_recursive(n):
    if n < 2:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_iterative(n):
    if n < 2:
        return n

    prev = 0
    curr = 1

    for i in range(2, n+1):
        next_fib = prev + curr
        prev = curr
        curr = next_fib

    return curr


print(fibonacci_iterative(5))
print(fibonacci_recursive(5))
