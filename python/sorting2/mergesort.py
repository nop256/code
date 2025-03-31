

def mergesort(numbers):
    if len(numbers) <= 1: # need this check, idk why
        return numbers
    
    
    mid = len(numbers) // 2
    left_half = numbers[:mid] # split into halves
    right_half = numbers[mid:] # split into halves
    
    
    left_sorted = mergesort(left_half) # recursion sorting
    right_sorted = mergesort(right_half) # recursion sorting
    
    return merge(left_sorted, right_sorted)

def merge(left, right):
    merged = []
    left_index = right_index = 0
    
    # comparing halves and sorting array
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
            
    
    merged.extend(left[left_index:]) # add leftovers
    merged.extend(right[right_index:]) # add leftovers
    
    return merged
    
A=[38, 27, 43, 3, 9, 82, 10]

newa = mergesort(A)
print(newa)