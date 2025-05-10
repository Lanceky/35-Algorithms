def insertion_sort(arr):
    for i in range(1, len(arr)):  # Start from the 2nd element
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:  # Shift elements > key right
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Insert key in its correct position
    return arr

# Test
array = [12, 11, 13, 5, 6]
print(insertion_sort(array))  # Output: [5, 6, 11, 12, 13]