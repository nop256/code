def merge_sort(numbers):
    if len(numbers) <= 1:  # Base case
        return numbers
    
    mid = len(numbers) // 2
    left_half = numbers[:mid]
    right_half = numbers[mid:]
    
    # Recursive sorting
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    merged = []
    left_index = right_index = 0
    
    # Merge while both lists have elements
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Add remaining elements from left and right (if any)
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged

# Example usage
A = [38, 27, 43, 3, 9, 82, 10]
newa = merge_sort(A)
print(newa)
