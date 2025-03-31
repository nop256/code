def counting(numbers, count):
    n = len(numbers)
    F = [0] * n  # Frequency array
    for a in numbers:
        count[0] += 1  # Count comparison
        F[a] += 1

    k = 0
    for value in range(n):
        for _ in range(F[value]):
            count[0] += 1  # Count assignment
            numbers[k] = value
            k += 1
