def bubble(numbers, count):
    n = len(numbers)
    flag = True
    while flag:  # Outer loop, iterate until no swaps are needed
        flag = False
        for i in range(0, n - 1):
            count[0] += 1
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                flag = True
