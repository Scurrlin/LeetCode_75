def fibonacci(n):
    if n <= 1:
        return n
    sequence = [0] * (n + 1)
    sequence[1] = 1
    for i in range(2, n + 1):
        sequence[i] = sequence[i - 1] + sequence[i - 2]
    return sequence[n]

print(fibonacci(10))