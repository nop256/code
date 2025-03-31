def shaker(numbers, count):
    n = len(numbers)
    flag = True
    while flag:
        flag = False
        # Right-to-left pass
        for i in range(n - 2, -1, -1):
            count[0] += 1
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                flag = True
        # Left-to-right pass
        for i in range(n - 1):
            count[0] += 1
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                flag = True
