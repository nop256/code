def suminout(nums, a, b):
    total = 0

    for num in nums:

        if num != a and num != b:
            total += num

    return total
