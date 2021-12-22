def fibonacci_of_n(n):
    if n in {0, 1}:
        return n
    return fibonacci_of_n(n-1) + fibonacci_of_n(n-2)