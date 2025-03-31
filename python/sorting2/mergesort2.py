def mergesort(numbers, count):
    if len(numbers) <= 1:  # Base case
        return numbers

    # Split the array into two halves
    mid = len(numbers) // 2
    left_half = numbers[:mid]
    right_half = numbers[mid:]

    # Recursive sorting
    left_sorted = mergesort(left_half, count)
    right_sorted = mergesort(right_half, count)

    # Merge the sorted halves
    i = j = k = 0
    while i < len(left_sorted) and j < len(right_sorted):
        count[0] += 1  # Count comparison
        if left_sorted[i] <= right_sorted[j]:
            numbers[k] = left_sorted[i]
            i += 1
        else:
            numbers[k] = right_sorted[j]
            j += 1
        k += 1

    # Copy leftovers from left half
    while i < len(left_sorted):
        numbers[k] = left_sorted[i]
        i += 1
        k += 1

    # Copy leftovers from right half
    while j < len(right_sorted):
        numbers[k] = right_sorted[j]
        j += 1
        k += 1

    return numbers
